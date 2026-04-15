# Neurowarp
# 🧠 NeuroWarp – Mind-Controlled Gaming using EEG

## 🚀 Overview

NeuroWarp is a Brain-Computer Interface (BCI) system that allows users to control games using brain signals (EEG) collected from the prefrontal cortex.

## 🎯 Problem

Traditional gaming requires physical input devices, making it inaccessible for individuals with motor impairments.

## 💡 Solution

We use EEG signals to detect brain activity and convert them into game controls using machine learning.

## ⚙️ How it works

EEG → Arduino → Serial → Python → CSV → ML Model → Game Control

## 🛠 Tech Stack

* Arduino UNO R4 Minima
* Python (NumPy, Pandas, Scikit-learn)
* Serial Communication
* Machine Learning Model

## 🔥 Features

* Real-time brain signal processing
* Low-cost setup
* Hands-free game control

## 📦 Setup

```bash
pip install -r requirements.txt
python collect.py
python prediction.py
```

## 📌 Inspiration

Inspired by open-source BCI research (UpsideDownLabs), but implemented with custom data pipeline and ML model.

## 👨‍💻 Team

* Harshan A
* Hari Baalaji R
* Jahir
* Hariharan
