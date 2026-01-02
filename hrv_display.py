"""
HRV feature display utilities
"""

import matplotlib.pyplot as plt

def display_hrv_features(hrv_features):
    """
    Display HRV features in a readable format.

    Parameters:
        hrv_features (dict): Dictionary containing HRV parameters
    """

    print("HRV PARAMETERS")
    print("----------------")
    for key, value in hrv_features.items():
        print(f"{key}: {value:.4f}")


def plot_rr_intervals(rr_intervals):
    """
    Plot RR intervals over time.

    Parameters:
        rr_intervals (list or array): RR interval values (seconds)
    """

    plt.figure(figsize=(6, 3))
    plt.plot(rr_intervals, marker="o", linestyle="-")
    plt.xlabel("Beat Number")
    plt.ylabel("RR Interval (s)")
    plt.title("RR Interval Variation")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
