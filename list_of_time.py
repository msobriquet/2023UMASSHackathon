import librosa
audio_file = librosa.load("Mannequin Pussy - Romantic.wav")
y,sr = audio_file
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#beats now contains the beat *frame positions*
#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
# convert the fram indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames,sr = sr)
#print(beat_times[0])

import librosa
audio_file = librosa.load("Mannequin Pussy - Romantic.wav")
y,sr = audio_file
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#beats now contains the beat *frame positions*
#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

import scipy
from scipy.io import wavfile

sample_rate, data = wavfile.read('Mannequin Pussy - Romantic.wav')
# note: sample/sec
len_data = len(data)

t = len_data / sample_rate
#print("Duration of audio in seconds: ", t)

list_of_time = []
t1 = beat_times[0] + 10
delta_t = tempo / 60
while t1 < t:
    list_of_time.append(t1)
    t1 += delta_t

print(list_of_time)
