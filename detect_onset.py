import librosa

file_path = 'audio/Mannequin Pussy - Romantic.wav'
x, fs = librosa.load(file_path, sr= )
onset_frames = librosa.onset.onset_detect(x, fs)
print(onset_frames)
onset_times = librosa.frames_to_time(onset_frames)
print(onset_times)

#, wait = 1, pre_avg=1, post_avg=1, pre_max=1, post_max=1