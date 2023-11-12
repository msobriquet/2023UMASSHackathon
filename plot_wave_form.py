'''#import module, libraries
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

#loading audio file
obj = wave.open("Mannequin Pussy - Romantic.wav", "r")

#get audio parameters
print("Parameters:", obj.getparams())

# number of samples per second
sample_freq = obj.getframerate()
#number of samples in the audio
n_samples = obj.getnframes()

#signal wave aka wave amplitude aka sound intensity
signal_wave = obj.readframes(-1)

#audio length aka duration of audio
duration = n_samples/sample_freq

#create numpy objects from the signal_wave, plotted on the y-axis
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

#create numpy object from duration --> plotted on x-axis
time = np.linspace(0, duration, num=n_samples)
time = np.linspace(0, duration, num=n_samples)
'''

signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()

if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

Time = np.linspace(0, len(signal) / fs, num=len(signal))

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(Time, signal)
plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# import wave
# import sys

# #loading audio file
# obj = wave.open("Mannequin Pussy - Romantic.wav", "r")

# #signal wave aka wave amplitude aka sound intensity
# signal_wave = obj.readframes(-1)


# if obj.getnchannels() == 2:
#     print("Just mono files")
#     sys.exit(0)

# plt.title("Signal Wave...")
# plt.plot(signal_wave, color = "blue")
# plt.ylabel("Amplitude")
# plt.show()