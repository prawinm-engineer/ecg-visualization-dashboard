"""
ECG serial data loader from Arduino
"""

import serial
import time

def read_ecg_from_serial(port="COM3", baudrate=9600, duration=10):
    """
    Reads ECG data from Arduino serial output.

    Parameters:
        port (str): Serial port (e.g., COM3 or /dev/ttyUSB0)
        baudrate (int): Baud rate for serial communication
        duration (int): Duration of data capture in seconds

    Returns:
        list: ECG signal values
    """

    ecg_data = []
    ser = serial.Serial(port, baudrate)
    time.sleep(2)  # Allow serial connection to stabilize

    start_time = time.time()

    while time.time() - start_time < duration:
        try:
            line = ser.readline().decode("utf-8").strip()
            if line.isdigit():
                ecg_data.append(int(line))
        except:
            continue

    ser.close()
    return ecg_data


if __name__ == "__main__":
    signal = read_ecg_from_serial()
    print(f"Captured {len(signal)} ECG samples")
