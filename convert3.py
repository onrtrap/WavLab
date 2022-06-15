import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open("ThereIsNoBanishedZone.wav", "r")
spf2 = wave.open("ThereIsNoBanishedZoneWah.wav", "r")

signal = spf.readframes(-1)
signal = np.frombuffer(signal, dtype=int)
signal2 = spf2.readframes(-1)
signal2 = np.frombuffer(signal2, dtype=int)

i = 0

wahsignal = []

# Multiplication increases the sound volume
print('Signal 1')
while i < len(signal):
    s = 0
    s = signal[i] + 600
    #    print(s)
    wahsignal.append(s)
    i += 1
outputFile = wave.open("wah.wav", "wb")
outputFile.setnchannels(spf.getnchannels())
outputFile.setframerate(spf.getframerate())
outputFile.setsampwidth(spf.getsampwidth())

# print(type(wahSignal))
outputFile.writeframes(np.array(wahsignal).tobytes())
outputFile.close()
print('done')
