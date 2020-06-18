# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:44:52 2020

@author: Alec
"""


from pydub import AudioSegment
from pydub.playback import play
import numpy as np
from sklearn.preprocessing import scale
from scipy.io.wavfile import read as wvr
import matplotlib.pyplot as plt

# music fileN
file = 'Because.mp4'
sound = AudioSegment.from_file(file, format='mp4')
#play(sound) # play the sound

# Write a .wav file for use with scipy
sound.export(file.split('.')[0] + '.wav', format='wav') 

# Re-read the sound
sound2 = AudioSegment.from_file('Because.wav', format='wav')
# play(sound2)


# Use scipy tp read in t
fs, data = wvr('Because.wav')
print(f'number of channels {data.shape[1]}')

print(f'shape {data.shape}')

length = data.shape[0] / fs
print(length)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
time = np.linspace(0., length, data.shape[0])
ax1.plot(time, data[:, 0], '-b',label='Left Channel')
ax2.plot(time, data[:, 1], '-r',label='Right Channel')
fig.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
