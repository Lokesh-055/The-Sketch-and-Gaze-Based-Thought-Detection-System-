# The-Sketch-and-Gaze-Based-Thought-Detection-System-
The Sketch and Gaze Based Thought Detection System is an AI-driven human–computer interaction project that analyzes eye gaze movements and sketch patterns to interpret user intentions. By combining computer vision, facial landmark detection, and sketch analysis, the system predicts thought patterns in real time. 👁️✏️🤖.By Lokesh M 

# Sketch and Gaze Based Thought Detection System

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Facial%20Tracking-orange)
![License](https://img.shields.io/badge/license-MIT-blue)


## Overview

The **Sketch and Gaze Based Thought Detection System** is an AI-based human-computer interaction system that predicts a user's thought process by analyzing:

- **Eye gaze movements**
- **Facial landmarks**
- **Sketch input patterns**

The system combines **computer vision and sketch analysis** to understand the user's intention or thought direction in real time.

This project integrates **gaze tracking and sketch recognition** to build an intelligent system capable of interpreting human behavior.

---
<img width="414" height="122" alt="image" src="https://github.com/user-attachments/assets/03560d0e-590e-42b9-97e0-11839ecbcd9b" />


## Features

- Real-time **Eye Gaze Tracking**
- **Sketch Pattern Recognition**
- Facial Landmark Detection using **MediaPipe**
- **Feature Extraction from Sketch and Eye Movements**
- Fusion of **Gaze + Sketch Data**
- Thought pattern prediction using Machine Learning

---

## System Architecture

<img width="634" height="551" alt="image" src="https://github.com/user-attachments/assets/36b325e8-9a32-43a6-ab7f-65babf8f323b" />


The system consists of several integrated modules:

### 1. Input Layer
Captures real-time data from:
- Webcam (for gaze tracking)
- Sketch input (mouse / touchscreen)

### 2. Preprocessing Layer
- Noise removal
- Data normalization
- Frame filtering

### 3. Feature Extraction Layer

#### Gaze Features
- Eye movement tracking
- Pupil position detection
- Facial landmark extraction using **MediaPipe**

#### Sketch Features
- Stroke direction
- Drawing speed
- Shape recognition using **OpenCV and NumPy**

### 4. Fusion Layer
Combines gaze and sketch features into a unified feature vector.

### 5. Prediction Layer
Uses machine learning models to interpret the combined features and determine the user's thought pattern.
<img width="1241" height="511" alt="image" src="https://github.com/user-attachments/assets/52c37e5b-65d8-4ea8-b8fb-13e015270cc5" />

---

## Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **NumPy**
- **Scikit-learn**
- **TensorFlow / PyTorch (optional)**

sketch-gaze-thought-detection
│
├── data
│
├── gaze_tracking
│   ├── gaze_detector.py
│
├── sketch_processing
│   ├── sketch_analyzer.py
│
├── fusion
│   ├── feature_fusion.py
│
├── models
│   ├── thought_model.py
│
├── main.py
├── requirements.txt
└── README.md


