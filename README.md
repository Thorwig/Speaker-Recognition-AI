<div align="center">
<h1 align="center">
<br>Speaker-Recognition-AI
</h1>
<h3>◦ A text-independent Speaker Recognition solution  </h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style&logo=SciPy&logoColor=white" alt="SciPy" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />

<img src="https://img.shields.io/badge/NumPy-013243.svg?style&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Flask-000000.svg?style&logo=Flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)

---


## 📍 Overview

The project is focused on speaker recognition AI and has multiple core functionalities. It includes features for noise reduction in audio, extracting MFCC features from audio files, training a Support Vector Machine (SVM) classifier on the extracted features, and predicting the labels of new audio files. The project's purpose is to provide a robust system for enrolling, identifying, and listing speakers based on their audio samples, offering value in applications such as voice-based authentication and speaker verification.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The system follows a modular architecture with a separation of concerns. It utilizes a client-server model with Flask as the web framework. It makes use of classification models trained using SVM and contains a MySQL database for data storage.|
| 🔗 | **Dependencies**   | The system relies on multiple external libraries such as Flask, joblib, librosa, numpy, scikit-learn, scipy, sounddevice, soundfile, and mysql_connector_repackaged. These libraries provide various functionalities such as web development, serialization, audio processing, database connectivity, noise reduction, numeric operations, machine learning, and scientific computing.|
| ⚡️ | **Performance**    | The performance of the system depends on the hardware used and the complexity of audio processing operations. After training this model with optimal condition, an accuracy score of 97% was obtained.|
| 🔌 | **Integrations**   | The codebase integrates with various external services, such as MySQL for database connectivity and Flask for web development. Enhancements could include integrating continuous integration (CI) tools like Jenkins or Travis CI for automated building and testing.|
---


## 📂 Repository Structure

```sh
└── Speaker-Recognition-AI/
    ├── Parameters/
    │   └── database_parameters.json
    ├── README.md
    ├── classifier.py
    ├── extract.py
    ├── extracted_features/
    │   ├── features.npy
    │   ├── labels.npy
    │   ├── predict_features.npy
    │   └── predict_labels.npy
    ├── feat_extract.py
    ├── feat_extract_predict.py
    ├── form.py
    ├── models/
    │   ├── trained_model_svm.joblib
    │   ├── trained_pca.joblib
    │   └── trained_scaler.joblib
    ├── read_npy.py
    ├── reduce_noise.py
    ├── requirements.txt
    ├── speaker_recognition/
    ├── static/
    │   ├── resources/
    │   │   ├── Enroll.jpg
    │   │   ├── Identification.jpg
    │   │   ├── Refresh.png
    │   │   ├── background.jpg
    │   │   ├── images.png
    │   │   └── list.jpg
    │   ├── scripts/
    │   │   ├── enroll.js
    │   │   ├── identification.js
    │   │   └── list.js
    │   ├── styles/
    │   │   └── form.css
    │   └── templates/
    │       ├── Identification.html
    │       ├── enroll.html
    │       ├── list.html
    │       └── users.json
    └── templates/
        └── form.html
```


---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [requirements.txt](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/requirements.txt)               | This code utilizes Flask for web development, joblib for serialization, librosa for audio processing, and mysql_connector_repackaged for database connectivity. It also includes functionalities for noise reduction, numeric operations using numpy, machine learning with scikit-learn, scientific computing with scipy, and audio handling using sounddevice and soundfile.                                                                                                                                                                                                                                                                                                                                                |
| [extract.py](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/extract.py)                           | This code snippet calculates the duration of an audio file, reduces noise in the audio using a separate module, and removes any directories that have fewer than 3 files in a given directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [feat_extract.py](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/feat_extract.py)                 | This code snippet processes audio files to extract MFCC features. It can either read from a specific file or capture audio from a device's input. The extracted features are then used to create a feature matrix. The code also handles error cases. The extracted features and corresponding labels are returned as numpy arrays.                                                                                                                                                                                                                                                                                                                                                                                           |
| [read_npy.py](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/read_npy.py)                         | The code reads and saves audio classification features and labels from numpy files. It prints the loaded labels and has commented out code to remove specific labels and corresponding features.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [reduce_noise.py](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/reduce_noise.py)                 | This code uses the scipy and noisereduce libraries to reduce noise in an audio file. It reads the audio file, applies noise reduction, and saves the cleaned audio as a new file. The file name is modified to indicate that it has been noise reduced. The function returns the path of the reduced file.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [classifier.py](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/classifier.py)                     | This code comprises two functions. The first function, "svm_classifier()", trains a Support Vector Machine (SVM) classifier on a given dataset. It preprocesses the data by scaling and applying Principal Component Analysis (PCA) for dimensionality reduction. The trained model, scaler, and PCA objects are saved for future use. The accuracy of the model on a test set is printed and returned.The second function, "svm_predict()", uses the trained model, scaler, and PCA objects to make predictions on a new dataset. It provides the predicted classes, a score indicating the confidence of the predictions, and a relevance matrix highlighting the top two predicted classes and their corresponding scores. |
| [form.py](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/form.py)                                 | This code is a Flask web application that allows users to enroll and identify themselves based on audio samples. It uses feature extraction, classification, and a MySQL database to support these functionalities. The code can handle audio file upload, transform audio from mp3 to wav format, extract features from audio, save features and labels, perform classification using SVM, and retrieve and delete data from the database.                                                                                                                                                                                                                                                                                   |
| [feat_extract_predict.py](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/feat_extract_predict.py) | The code allows for extracting features from audio files and predicting their labels. It uses the Librosa library to compute MFCC features, and extracts statistical characteristics such as mean, standard deviation, skewness, maximum value, median, and minimum value. It can process either a specified file or audio input from a device. The extracted features are then used to train a machine learning model for classification.                                                                                                                                                                                                                                                                                    |

</details>

<details closed><summary>Templates</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                    |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                        |
| [form.html](https://github.com/Thorwig/Speaker-Recognition-AI/blob/main/templates/form.html) | This code is a basic HTML template that creates a speaker recognition web application. It includes a navigation menu and three sections for enrolling, listing, and identifying speakers. Each section has a button and an image. The code also includes a placeholder for displaying verification output. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Python version 3.7 and above`

1. Clone the Speaker-Recognition-AI repository:
```sh
git clone https://github.com/Thorwig/Speaker-Recognition-AI
```

2. Change to the project directory:
```sh
cd Speaker-Recognition-AI
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```
4. Run the program
```sh
python main.py
```
