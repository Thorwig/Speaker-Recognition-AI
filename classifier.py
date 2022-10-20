import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import joblib


def svm_classifier():
    X =  np.load('extracted_features/features.npy',allow_pickle=True)
    y =  np.load('extracted_features/labels.npy').ravel()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pca = PCA(n_components=20)
    pca.fit(X_train)
    X_t_train = pca.transform(X_train)
    X_t_test = pca.transform(X_test)
    filename2 = "models/trained_pca.joblib"
    joblib.dump(pca,filename2)
    

    clf = SVC(C=10, gamma=0.00001,kernel='rbf')
    clf.fit(X_t_train, y_train)
    acc = clf.score(X_t_test, y_test)
    print(acc)
    print("acc=%0.3f" % acc)   
    filename = "models/trained_model_svm.joblib"
    joblib.dump(clf,filename)
    print('Success')
    return filename

def svm_predict():
    X =  np.load('extracted_features/predict_features.npy')
    
    filename2 = "models/trained_pca.joblib"
    filename = "models/trained_model_svm.joblib"
    pca = joblib.load(filename2)
    X_t = pca.transform(X)
    clf = joblib.load(filename)
    predict_x = clf.predict(X_t)
    score = clf.decision_function(X_t)
    score = (max(score[0]) / len(score[0]))/1.3
    print(predict_x)
    return predict_x, score

