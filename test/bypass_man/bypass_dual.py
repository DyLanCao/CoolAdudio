import numpy as np
from scipy.io import wavfile
from scipy import signal

def splitChannel(srcMusicFile,srcMusicFile1):
    # read wav file
    sampleRate, musicData = wavfile.read(srcMusicFile)
    sampleRate, musicData1 = wavfile.read(srcMusicFile1)

    left = []
    right = []
    for item in musicData:
        left.append(item)

    for item1 in musicData1:
        right.append(item1)

    mixed_data = np.array(right) - np.array(left)
    wavfile.write('mixed_data.wav', sampleRate, mixed_data)

splitChannel("leftc.wav","right.wav")


