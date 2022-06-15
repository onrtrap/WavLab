import matplotlib.pyplot as plt
import numpy as np
import wave
import scipy.fftpack

spf = wave.open("ThereIsNoBanishedZone.wav", "r")
spf2 = wave.open("ThereIsNoBanishedZone.wav", "r")

signal = spf.readframes(-1)
signal = np.frombuffer(signal, dtype=int)
sp = np.fft.fft(signal)
n = signal.size
timestep = 0.1
freq = np.fft.fftfreq(n, d=timestep)
#plt.plot(freq, sp.real, freq, sp.imag)
#plt.show()

i = 0

while i < len(freq):
    s = 0
    s = freq[i] + 600
    print(s)

    i += 1

signal = spf2.readframes(-1)
signal = np.frombuffer(signal, dtype=int)
sp = np.fft.fft(signal)
n = signal.size
timestep = 0.1
freq = np.fft.fftfreq(n, d=timestep)
#plt.plot(freq, sp.real, freq, sp.imag)
#plt.show()

i = 0

print('Starting file 2.')

while i < len(freq):
    s = 0
    s = freq[i] + 600
    print(s)

    i += 1