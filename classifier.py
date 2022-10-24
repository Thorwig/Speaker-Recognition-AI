import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib
from sklearn.decomposition import PCA
from sklearn import preprocessing
def svm_classifier():
# Load data from numpy file
    X =  np.load('extracted_features/features.npy',allow_pickle=True)
    y =  np.load('extracted_features/labels.npy').ravel()

    # Split data into training and test subsets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = preprocessing.StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    filename3 = "models/trained_scaler.joblib"
    joblib.dump(scaler,filename3)

    # defining parameter range
    
    pca = PCA(n_components=0.95)
    pca.fit(X_train)
    X_t_train = pca.transform(X_train)
    X_t_test = pca.transform(X_test)
    filename2 = "models/trained_pca.joblib"
    joblib.dump(pca,filename2)
    # Simple SVM
    print('fitting...')
    clf = SVC(C=100, gamma=0.0001 ,kernel='rbf', probability=True)
    clf.fit(X_t_train, y_train)
    acc = clf.score(X_t_test, y_test)
    print(acc)
    print("acc=%0.3f" % acc)   
    filename = "models/trained_model_svm.joblib"
    joblib.dump(clf,filename)
    print('Success')
    return acc

def svm_predict():
    X =  np.load('extracted_features/predict_features.npy')
    print('fitting...')
    filename3 = "models/trained_scaler.joblib"
    filename2 = "models/trained_pca.joblib"
    filename = "models/trained_model_svm.joblib"
    scaler = joblib.load(filename3)
    X = scaler.transform(X)
    pca = joblib.load(filename2)
    X_t = pca.transform(X)
    clf = joblib.load(filename)
    predict_x = clf.predict(X_t)
    print(clf.predict_proba(X_t)[0])
    print(predict_x)
    score = 1 - min(clf.predict_proba(X_t)[0])*100

    return predict_x, score

