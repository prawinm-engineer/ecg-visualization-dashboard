"""
ECG waveform visualization
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_ecg_signal(ecg_signal, fs=200):
    """
    Plot ECG waveform.

    Parameters:
        ecg_signal (list or array): ECG data samples
        fs (int): Sampling frequency in Hz
    """

    ecg_signal = np.array(ecg_signal)
    time_axis = np.arange(len(ecg_signal)) / fs

    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, ecg_signal, color="blue", linewidth=1)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("ECG Waveform")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Example usage with dummy data
    dummy_ecg = np.sin(2 * np.pi * 1 * np.linspace(0, 5, 1000))
    plot_ecg_signal(dummy_ecg)
