import os
import wave
import contextlib
import shutil
from reduce_noise import noise_reduce


def audio_length(fname):
    with contextlib.closing(wave.open(noise_reduce(fname),'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration

directory = 'D:/dataset/librispeech2/voices_extracted/'

for i in os.listdir(directory):
    path = directory + i + '/'
    if len(os.listdir(path)) < 3:
        shutil.rmtree(path)




