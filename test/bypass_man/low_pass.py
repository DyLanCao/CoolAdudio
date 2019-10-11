from scipy.io import wavfile
from scipy import signal
import numpy as np

sr, x = wavfile.read('mixed_data.wav')      # 16-bit mono 44.1 khz

b = signal.firwin(101, cutoff=300, fs=sr, pass_zero=True)

x = signal.lfilter(b, [1.0], x)

wavfile.write('mixed_low.wav', sr, x.astype(np.int16))
