import librosa
audio_file = librosa.load("Mannequin Pussy - Romantic.wav")
y,sr = audio_file
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#beats now contains the beat *frame positions*
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

import scipy
from scipy.io import wavfile

sample_rate, data = wavfile.read('Mannequin Pussy - Romantic.wav')
# note: sample/sec
len_data = len(data)

t = len_data / sample_rate
print("Duration of audio in seconds: ", t)


file_path = 'audio/Mannequin Pussy - Romantic.wav'
x, fs = librosa.load(file_path, sr= sample_rate)
onset_frames = librosa.onset.onset_detect(x)
print(onset_frames)
onset_times = librosa.frames_to_time(onset_frames)
print(onset_times)