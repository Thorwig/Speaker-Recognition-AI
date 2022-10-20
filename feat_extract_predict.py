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

def parse_predict_files(parent_dir,file_ext='*.wav'):
    features, labels = np.empty((0,180)), np.empty(0)
    for fn in glob.glob(os.path.join(parent_dir, file_ext)):
        mfccs = extract_feature(fn)
        ext_features = np.hstack((np.mean(mfccs, axis=1), np.std(mfccs, axis=1), skew(mfccs, axis = 1), np.max(mfccs, axis = 1), np.median(mfccs, axis = 1), np.min(mfccs, axis = 1)))
        features = np.vstack([features,ext_features])
        labels = [0]
        print("extract %s features done" % fn)
    return np.array(features), np.array(labels)


