import wave
import numpy as np
import matplotlib.pyplot as plt

# Load the WAV file
wav_file = wave.open('Mannequin Pussy - Romantic.wav', 'rb')

# Get the audio data
frames = wav_file.readframes(-1)
signal = np.frombuffer(frames, dtype='int16')

# Get the frame rate (number of frames per second)
frame_rate = wav_file.getframerate()

# Get the duration of the audio in seconds
duration = len(signal) / frame_rate

# Create the time axis for the waveform
time = np.linspace(0, duration, num=len(signal))

# Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(time, signal, color='b')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Waveform')
plt.grid(True)
plt.show()

# Close the WAV file
wav_file.close()