import librosa
audio_file = librosa.load("Mannequin Pussy - Romantic.wav")
y,sr = audio_file
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#beats now contains the beat *frame positions*
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
#convert the fram indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames,sr = sr)
print(beat_times)



#output of beat_track is based on estimated tempo & position of detected note onsets
#-> if the deteced beats are too rigidly speaced -> reduce tighteness parameter 
