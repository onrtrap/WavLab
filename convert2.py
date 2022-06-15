import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


def switch_wave(num, index, arr, arr2):
    switcher = {
        0: arr[index],
        1: arr[index],
        2: arr[index],
        3: arr[index],
        4: arr2[index],
        5: arr2[index],
        6: arr2[index]
    }
    return switcher.get(num, "0")


spf = wave.open("Generic Beach Loop.wav", "r")
spf2 = wave.open("March Of The Bees.wav", "r")

signal = spf.readframes(-1)
signal = np.frombuffer(signal, dtype=int)
signal2 = spf2.readframes(-1)
signal2 = np.frombuffer(signal2, dtype=int)
print(signal)

splicedSignal = []
i = 0
length = 0

if len(signal) <= len(signal2):
    length = len(signal)
else:
    length = len(signal2)
val = 0
while i < length:
    s = 0
    s = switch_wave(val, i, signal, signal2)
    splicedSignal.append(s)
    i += 1

    val += 1
    if val >= 6:
        val = 0

print("exporting to spliced.wav")
outputFile = wave.open("spliced.wav", "wb")
outputFile.setnchannels(spf.getnchannels())
outputFile.setframerate(spf.getframerate())
outputFile.setsampwidth(spf.getsampwidth())

# print(type(splicedSignal))
outputFile.writeframes(np.array(splicedSignal).tobytes())
outputFile.close()
print("done")
