import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load the WAV file
wav_file = 'Mannequin Pussy - Romantic.wav'

# Load the audio data and its sampling rate
y, sr = librosa.load(wav_file)

# Compute the onset strength envelope
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# Estimate the tempo and beat frames
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, onset_envelope=onset_env)

# Convert beat frames to time
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Plot the waveform and beat events
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform')
plt.subplot(2, 1, 2)
librosa.display.waveshow(y, sr=sr)
plt.vlines(beat_times, -1, 1, color='r', alpha=0.7, label='Beats')
plt.title('Beats')
plt.tight_layout()
plt.show()