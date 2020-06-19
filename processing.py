# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:38:20 2020

@author: Alec
"""

from youtube_dl import YoutubeDL as ydl
import os
from pydub import AudioSegment
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display


def download_song(link, directory=None):
    """
    

    Parameters
    ----------
    link : str or list
        youtube link or links in which to download video from
    directory : str
        location of where file will be saved

    Returns
    -------
    None.

    """
    if directory:
        # Create directory if it does not exist
        if not os.path.exists(directory):
            os.mkdir(directory)
        # Change working directory to new directory to download songs into
        os.chdir(directory)
    
    if isinstance(link, str):
        link = [link]
    
    # Create hook to pring out when the downloading has finished
    def my_hook(d):
        if d['status'] == 'finished':
            print('Finished downloading...')
    
    ydl_opts = {
        'progress_hook': [my_hook]
        }
    # download link
    with ydl(ydl_opts) as dl:
        dl.download(url_list=link)
    
    
    
def convert_mp4_to_wav(file, outdir=None):
    """
    

    Parameters
    ----------
    file : TYPE
        DESCRIPTION.
    outdir : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    """
    
    # Set wav extension
    wav = '.wav'
    
    if not outdir:
        # Get the directory name to save to
        outdir = os.path.dirname(file)
    else:
        # If directory does not exist, create so
        if not os.path.exists(outdir):
            os.mkdir(outdir)
            
    # Get the file name and the extension
    base_file, ext = os.path.splitext(os.path.basename(file))

    # Import the sound as an AudioSegment
    sound = AudioSegment.from_file(file)
    sound = sound.set_channels(1)
    new_file = os.path.join(outdir, base_file + wav)
    sound.export(new_file, format="wav")
    print("Successfully created", new_file)
    
    
def download_albums(down_dir): 
    """
    

    Parameters
    ----------
    down_dir : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for key in down_dir.keys():
        print("Starting on %s..." % key)
        direc = down_dir[key]['directory']
        link = down_dir[key]['link']
        print("Fetching the web address")
        download_song(link, direc)
    
        
def plot_spectrogram(file, outdir=None):
    """


    Parameters
    ----------
    file : TYPE
        DESCRIPTION.
    outdir : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    """
    if not outdir:
        # Get the directory name to save to
        outdir = os.path.dirname(file)
    else:
        # If directory does not exist, create so
        if not os.path.exists(outdir):
            os.mkdir(outdir)
    
    base_file, ext = os.path.splitext(os.path.basename(file))
    image_path = os.path.join(outdir, base_file + '.png')
    
    sample_rate, samples = wavfile.read(file)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
    
    fig, ax = plt.subplots(1, 1, figsize=(0.72,0.72))
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    ax.pcolormesh(times, frequencies, np.log(spectrogram), cmap=plt.cm.jet)   
    plt.savefig(image_path, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()
    fig.clf()
    plt.close(fig)
    print("Successfully created...", image_path)
    
    
def plot_melspectrogram(file, outdir=None, x_axis="time", y_axis="log"):
    
    
    if not outdir:
        # Get the directory name to save to
        outdir = os.path.dirname(file)
    else:
        # If directory does not exist, create so
        if not os.path.exists(outdir):
            os.mkdir(outdir)
            
    base_file, ext = os.path.splitext(os.path.basename(file))
    image_path = os.path.join(outdir, base_file + '.png')
    
    audio, sr = librosa.load(file)
    
    fig, ax = plt.subplots(1, 1, figsize=(1,1))
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    mel = librosa.feature.melspectrogram(y=audio, sr=sr)
    librosa.display.specshow(librosa.power_to_db(mel), 
                             x_axis=x_axis, y_axis=y_axis)
    plt.savefig(image_path, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()
    fig.clf()
    plt.close(fig)
    print("Successfully created...", image_path)
    

def plot_stft(file, outdir=None, x_axis="time", y_axis="log"):
    
    
    if not outdir:
        # Get the directory name to save to
        outdir = os.path.dirname(file)
    else:
        # If directory does not exist, create so
        if not os.path.exists(outdir):
            os.mkdir(outdir)
            
    base_file, ext = os.path.splitext(os.path.basename(file))
    image_path = os.path.join(outdir, base_file + '.png')
    
    audio, sr = librosa.load(file)
    
    fig, ax = plt.subplots(1, 1, figsize=(1,1))
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    stft = librosa.core.stft(y=audio)
    librosa.display.specshow(librosa.power_to_db(stft), 
                             x_axis=x_axis, y_axis=y_axis)
    plt.savefig(image_path, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()
    fig.clf()
    plt.close(fig)
    print("Successfully created...", image_path)
    
    
            
    