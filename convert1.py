import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open("Generic Beach Loop.wav", "r")
signal = spf.readframes(-1)
signal = np.frombuffer(signal, dtype=int)
print(signal)

plt.figure(1)
plt.xlim(0, 300000)
plt.title("Original Signal")
plt.ylim(-50000, 50000)
plt.plot(signal)
plt.show()

shelf = 25000
preClickEcho = 500
clickEcho = 10000

trimmedSignal = []
i = 0
while i < len(signal):
    s = signal[i]
    s += 4
    trimmedSignal.append(s)
    i += 1

plt.figure(1)
plt.xlim(0, 300000)
plt.title("Original Signal")
plt.ylim(-50000, 50000)
plt.plot(signal)

plt.figure(2)
plt.title("Without the section between clicks")
plt.plot(trimmedSignal)
plt.xlim(0, 300000)
plt.ylim(-50000, 50000)

plt.show()

print("exporting to trimmed.wav")
outputFile = wave.open("trimmed.wav", "wb")
outputFile.setnchannels(spf.getnchannels())
outputFile.setframerate(spf.getframerate())
outputFile.setsampwidth(spf.getsampwidth())

# print(type(trimmedSignal))
outputFile.writeframes(np.array(trimmedSignal).tobytes())
outputFile.close()
print("done")
