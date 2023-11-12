import librosa
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import os
import scipy.signal

threshold = 0.1
hop_length = 512
input_path = 'Mannequin Pussy - Romantic.wav'

y, sr = librosa.load(input_path, sr=None)
rms = librosa.feature.rms(y, hop_length=hop_length)[0, :]
peak_locs = scipy.signal.find_peaks(rms, height=threshold)[0]
peak_heights = rms[peak_locs]

times = librosa.times_like(rms, hop_length=hop_length, sr=sr)
plt.plot(times, rms, label="Energy (RMS)");
plt.plot(times, threshold*np.ones_like(rms), '--', label="Threshold")
plt.plot(times[peak_locs], peak_heights, 'o', label="Detected peaks")

plt.xlim(0, np.ceil(librosa.get_duration(y, sr)))
plt.xlabel("Time (s)")
plt.ylim(0, 2*threshold)
plt.title("Downbeat tracking of {}".format(os.path.split(input_path)[1]))
plt.legend()




#i should have a waveform here to track the real beats