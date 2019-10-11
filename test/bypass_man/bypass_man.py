import numpy as np
from scipy.io import wavfile
from scipy import signal

def splitChannel(srcMusicFile):
    # read wav file
    sampleRate, musicData = wavfile.read(srcMusicFile)

    left = []
    right = []
    for item in musicData:
        left.append(item[0])
        right.append(item[1])

    mixed_data = np.array(left) - np.array(right)
    wavfile.write('mixed_b.wav', sampleRate, mixed_data)

splitChannel("test.wav")


