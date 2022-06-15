import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open("ThereIsNoBanishedZone.wav", "r")
spf2 = wave.open("ThereIsNoBanishedZoneWah.wav", "r")

signal = spf.readframes(-1)
#signal = np.frombuffer(signal, dtype=int)
signal2 = spf2.readframes(-1)
#signal2 = np.frombuffer(signal2, dtype=int)

i = 0
print('Signal 1')
while i < 100:
    print(signal[i])

    i += 1

print('Signal 2')
j = 0

while j < 100:
    print(signal2[j])
    j += 1
