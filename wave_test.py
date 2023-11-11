import wave
import matplotlib.pyplot as plt

obj = wave.open("sample-file-1.wav", "rb")

print(obj.getnchannels())

print(obj.getframerate)