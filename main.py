"""
Main ECG Visualization and HRV Analysis Dashboard
"""

from ecg_serial_loader import read_ecg_from_serial
from ecg_visualization import plot_ecg_signal
from scipy.signal import find_peaks
import numpy as np

from hrv_display import display_hrv_features, plot_rr_intervals


def compute_rr_intervals(ecg_signal, fs=200):
    """
    Detect R-peaks and compute RR intervals.
    """

    peaks, _ = find_peaks(ecg_signal, distance=0.6 * fs)
    rr_intervals = np.diff(peaks) / fs
    return rr_intervals


def extract_hrv_features(rr_intervals):
    """
    Extract basic time-domain HRV features.
    """

    return {
        "Mean_RR": np.mean(rr_intervals),
        "SDNN": np.std(rr_intervals),
        "RMSSD": np.sqrt(np.mean(np.diff(rr_intervals) ** 2))
    }


if __name__ == "__main__":

    print("Starting ECG Visualization Dashboard...")

    # Step 1: Acquire ECG data from Arduino
    ecg_signal = read_ecg_from_serial(duration=10)

    # Step 2: Visualize ECG waveform
    plot_ecg_signal(ecg_signal)

    # Step 3: Compute RR intervals
    rr_intervals = compute_rr_intervals(ecg_signal)

    # Step 4: Plot RR intervals
    plot_rr_intervals(rr_intervals)

    # Step 5: Display HRV parameters
    hrv_features = extract_hrv_features(rr_intervals)
    display_hrv_features(hrv_features)
