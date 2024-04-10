<div align="center">
<h1 align="center">
<br>Speaker-Recognition-AI
</h1>
<h3>◦ A text-independent Speaker Recognition solution  </h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
    
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Flask-000000.svg?style&logo=Flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📂 Repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)

---


## 📍 Overview

The project is focused on speaker recognition AI and has multiple core functionalities. It includes features for noise reduction in audio, extracting MFCC features from audio files, training a Support Vector Machine (SVM) classifier on the extracted features, and predicting the labels of new audio files. The project's purpose is to provide a robust system for enrolling, identifying, and listing speakers based on their audio samples, offering value in applications such as voice-based authentication and speaker verification.

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
