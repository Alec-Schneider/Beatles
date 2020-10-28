# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 06:48:34 2020

@author: Alec
"""


import keras
from keras import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import (Conv2D, Dense, GlobalAveragePooling2D, Dropout,
                          MaxPooling2D)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

        

def create_cnn2D(input_shape, classes, conv_layers=4, filters=32, 
                 kernel_size=(3,3), padding='same', pool_size=(2,2), 
                 conv_activation="relu", dropout_rate=0.0, 
                 dense_activation='softmax', global_avg_pool=True,
                 optimizer="Adam", loss="categorical_crossentropy", 
                 **hyper_params):
    """
    Build and compile a keras 2D Convolutional Neural Network using any choice
    of optimizer and loss function.

    Parameters
    ----------
    input_shape : tuple of int and None type for batch_size
        Dimensions of the input images in the order of 
        (batch_size, height, width, channels) 
    classes : int
        number of class labels in the training data
    conv_layers : int, optional
        Number of convolutional layers to build into the mode. The default is 
        4.
    filters : int, optional
        The dimensionality of the output space (i.e. the number of output 
        filters in the convolution). The default is 32.
    kernel_size : tuple of ints, optional
        Specifying the height and width of the 2D convolution window. The 
        default is (3,3).
    padding : string, optional
        One of "valid" or "same" (case-insensitive). The default is 'same'.
    pool_size : tuple of integers, optional
        Window size over which to take the maximum. The default is (2,2).
    conv_activation : str, optional
        Activation function to use in the convolutional layers. The default is
        "relu".
    dropout_rate : float, optional
        Percentage of observations to remove after the convolutional layers. 
        The default is 0.0.
    dense_activation : str, optional
        Activation function to use in the Dense layer for prediction. The 
        default is 'softmax'.
    global_avg_pool : boolean, optional
        If True, add a global average pooling layer to the end of the model. 
        The default is True.
    optimizer : str, optional
        Function to optimize in model training. The default is "Adam".
    loss : str, optional
        Loss function to used to compute loss between true and predicted
        labels. The default is "categorical_crossentropy".
    **hyper_params : keras.optimizers parameters, optional
        Optional paramters that can be passed to a keras optimizer.

    Returns
    -------
    model : keras.engine.sequential.Sequential
        Compiled keras 2D Convolutional Neural Network.

    """
    dropout_layers = conv_layers // 2 # dropout for each layer
    pooling_layers = conv_layers - 1
    
    model = keras.Sequential()
    for i in range(conv_layers):
        model.add(Conv2D(filters, kernel_size, padding=padding, 
                         activation=conv_activation))
        filters *= 2
        if (i + 1) <= pooling_layers:
            model.add(MaxPooling2D(pool_size))
        if (i + 1) <= dropout_layers:
            model.add(Dropout(rate=dropout_rate))
            
    if global_avg_pool:
        model.add(GlobalAveragePooling2D())
    
    if classes == 2:
        model.add(Dense(1, activation=dense_activation))
    else:
        model.add(Dense(classes, activation=dense_activation))
    model.build(input_shape=input_shape)
    
    if optimizer.lower() == "sgd":
        optimizer = keras.optimizers.SGD(**hyper_params)
    elif optimizer.lower() == "adam":
        optimizer = keras.optimizers.Adam(**hyper_params)
        
    model.compile(optimizer=optimizer, loss=loss.lower(), metrics=["accuracy"])
    
    return model


def fetch_images_dataframe(dataframe, x_col, y_col, directory, batch_size=32, 
                           target_size=(64,64), class_mode="categorical", 
                           shuffle=False, seed=None,
                           validation_split=0.0, save_format="png"):
    """
    Use the keras ImageDataGenerator to load a training and validation set or
    a test set of images for model training or evaluation. Images will be
    scaled  down by 1/255.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        DataFrame object containing the image filename and its label. 
    x_col : str
        Column name containing the filenames of the images to load.
    y_col : str
        Column name containing the labels of the images that will be loaded.
    directory : str
        Path containing the images to be used in the model.
    batch_size : int, optional
        Batch size to be used in the generator. The default is 32.
    target_size : tuple, optional
        Tuple of integers that contains the size dimensions of the images. 
        The default is (64,64).
    class_mode : string, optional
        Categorical or binary class mode options that is dependent on the
        amount of labels in the training set. The default is "categorical".
    shuffle : boolean, optional
        If True, shuffles the images. The default is False.
    seed : int, optional
        Random seed. The default is None.
    validation_split : float, optional
        Portion of the images to be used in model validation. The default is 
        0.0.
    save_format : str, optional
        Image file type to be used. The default is "png".

    Returns
    -------
    Generator
        A generators containing the numpy array of the images and the 
        corresponding labels.

    """
    data_gen = ImageDataGenerator(rescale=1./255., 
                                  validation_split=validation_split)
    
    if validation_split:
        train_gen = data_gen.flow_from_dataframe(dataframe=dataframe,
                                        directory=directory,
                                        x_col=x_col,
                                        y_col=y_col,
                                        batch_size=batch_size,
                                        target_size=target_size,
                                        class_mode=class_mode,
                                        shuffle=shuffle,
                                        seed=seed,
                                        subset="training",
                                        save_format=save_format
                                       )
        valid_gen = data_gen.flow_from_dataframe(dataframe=dataframe,
                                        directory=directory,
                                        x_col=x_col,
                                        y_col=y_col,
                                        batch_size=batch_size,
                                        target_size=target_size,
                                        class_mode=class_mode,
                                        shuffle=shuffle,
                                        seed=seed,
                                        subset="validation",
                                        save_format=save_format
                                       )
        return train_gen, valid_gen
    else:
        test_gen = data_gen.flow_from_dataframe(dataframe=dataframe,
                                        directory=directory,
                                        x_col=x_col,
                                        y_col=y_col,
                                        batch_size=batch_size,
                                        target_size=target_size,
                                        class_mode=class_mode,
                                        shuffle=shuffle,
                                        seed=seed,
                                        save_format=save_format
                                       )
        return test_gen
    
    

def plot_loss_and_acc(history):
    """
    Plot the loss and accuracy of the training and validation set at each epoch
    during training.

    Parameters
    ----------
    history : TYPE
        Accuracy and losses over the epochs during the training of a model.

    Returns
    -------
    None.

    """
    hist = history.history
    x_arr = np.arange(len(hist['loss'])) + 1
    fig = plt.figure(figsize=(12,4))
    ax = fig.add_subplot(1,2,1)
    ax.plot(x_arr, hist['loss'], '-o', label='Train loss')
    ax.plot(x_arr, hist['val_loss'], '--<', label='Validation loss')
    ax.legend(fontsize=15)
    ax.set_xlabel('Epoch', size=15)
    ax.set_ylabel('Loss', size=15)

    ax = fig.add_subplot(1,2,2)
    ax.plot(x_arr, hist['accuracy'], '-o', label='Train acc.')
    ax.plot(x_arr, hist['val_accuracy'], '--<', label='Validation acc.')
    ax.legend(fontsize=15)
    ax.set_xlabel('Epoch', size=15),
    ax.set_ylabel('Accuracy', size=15)
    plt.show()
    