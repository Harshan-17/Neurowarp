import serial
import numpy as np
import pandas as pd
import time
import pickle
import pyautogui
from collections import deque
from scipy.signal import welch

# ========================
# CONFIG
# ========================
PORT = 'COM9'
BAUD = 115200
WINDOW_SIZE = 256
SAMPLING_RATE = 512

# ========================
# LOAD MODEL
# ========================
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# ========================
# FEATURE EXTRACTION (SIMPLIFIED)
# ========================
def extract_features(signal_data):
    freqs, psd = welch(signal_data, fs=SAMPLING_RATE)

    # Basic band power
    alpha = np.sum(psd[(freqs >= 8) & (freqs <= 13)])
    beta = np.sum(psd[(freqs >= 14) & (freqs <= 30)])

    ratio = alpha / beta if beta > 0 else 0

    return np.array([alpha, beta, ratio]).reshape(1, -1)

# ========================
# MAIN LOOP
# ========================
def main():
    ser = serial.Serial(PORT, BAUD, timeout=1)
    model = load_model()

    buffer = deque(maxlen=WINDOW_SIZE)

    print("NeuroWarp Running...")

    while True:
        try:
            data = ser.readline().decode().strip()

            if data:
                value = float(data)
                buffer.append(value)

                if len(buffer) == WINDOW_SIZE:
                    signal_array = np.array(buffer)

                    features = extract_features(signal_array)
                    prediction = model.predict(features)[0]

                    print("Prediction:", prediction)

                    # CONTROL
                    if prediction == 0:
                        pyautogui.press('space')
                    elif prediction == 1:
                        pyautogui.press('w')

                    buffer.clear()

        except Exception as e:
            print("Error:", e)

# ========================
if __name__ == "__main__":
    main()
