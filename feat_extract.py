import glob
import os
import librosa
import numpy as np
import soundfile as sf
import sounddevice as sd
import queue
from scipy.stats import skew
import reduce_noise

def extract_feature(file_name=None):
    if file_name: 
        print('Extracting', file_name)
        X, sample_rate = sf.read(file_name, dtype='float32')
    else:  
        device_info = sd.query_devices(None, 'input')
        sample_rate = int(device_info['default_samplerate'])
        q = queue.Queue()
        def callback(i,f,t,s): q.put(i.copy())
        data = []
        with sd.InputStream(samplerate=sample_rate, callback=callback):
            while True: 
                if len(data) < 100000: data.extend(q.get())
                else: break
        X = np.array(data)

    if X.ndim > 1: X = X[:,0]
    X = X.T

    mfccs = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=30)
    return mfccs

def parse_audio_files(parent_dir,file_ext='*.wav'):
    sub_dirs = os.listdir(parent_dir)
    sub_dirs.sort()
    features, labels = np.empty((0,180)), np.empty(0)
    for label, sub_dir in enumerate(sub_dirs):
        if os.path.isdir(os.path.join(parent_dir, sub_dir)):
            for fn in glob.glob(os.path.join(parent_dir, sub_dir, file_ext)):
                try: mfccs = extract_feature(fn)
                except Exception as e:
                    print("[Error] extract feature error in %s. %s" % (fn,e))
                    continue
                ext_features = np.hstack((np.mean(mfccs, axis=1), np.std(mfccs, axis=1), skew(mfccs, axis = 1), np.max(mfccs, axis = 1), np.median(mfccs, axis = 1), np.min(mfccs, axis = 1)))
                features = np.vstack([features,ext_features])
                if os.path.exists('extracted_features/labels.npy'):
                    label = [np.load('extracted_features/labels.npy')[-1] + 1]
                labels = np.append(labels, label)
            print("extract %s features done" % (sub_dir))
    return np.array(features), np.array(labels, dtype = np.int)


