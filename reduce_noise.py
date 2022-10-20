from scipy.io import wavfile
import noisereduce as nr
import os

def noise_reduce(filename):
    rate, data = wavfile.read(filename)
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    filename2 = os.path.splitext(filename)[0] + "_reduced.wav"
    wavfile.write(filename2, rate, reduced_noise)
    return filename2

