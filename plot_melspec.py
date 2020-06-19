# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:59:44 2020

@author: Alec
"""


import os
import processing


def write_plots(walk):
    # get the path, subfolders, and files in each tuple
    for path, dirs, files in walk:
        # split the path to get the directory minus the last folder
        dirname, end = os.path.split(path)
        # check if it is one of our downloaded files
        if end == "wav":
            dirname, album = os.path.split(dirname)
            dirname, artist = os.path.split(dirname)
            for file in files:
                # file to download
                file_path = os.path.join(path, file)
                # laction to save converted file
                if artist == "Beatles":
                    new_path = os.path.join(dirname, "test_melspec")
                else:
                    new_path = os.path.join(dirname, "train_melspec")
                # pass to converter function
                processing.plot_melspectrogram(file_path,
                                              new_path)




if __name__ == '__main__':
    base_dir = 'C:\\Users\\Alec\\MyPython\\Beatles\\'

    dirs = ["Beatles", "lennon", "mccartney", "harrison", "starr"]
    
    # walk each of the designated paths
    walks =  [os.walk(os.path.join(base_dir, i)) for i in dirs]
    walks = [list(walk) for walk in walks]
    import multiprocessing as mp
    with mp.Pool(5) as p:
        p.map(write_plots, walks)