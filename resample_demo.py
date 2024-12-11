# Import necessary libraries
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For visualizations
from scipy.signal import resample  # For signal resampling

# Generate a sine wave signal
def generate_signal(frequency=5, sampling_rate=100, duration=1):
    """
    Generates a sine wave signal.

    Parameters:
        frequency (float): Frequency of the sine wave in Hz.
        sampling_rate (int): Sampling rate in samples per second.
        duration (float): Duration of the signal in seconds.

    Returns:
        tuple: Time array and signal array.
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # Time array
    signal = np.sin(2 * np.pi * frequency * t)  # Sine wave
    return t, signal

# Resample the signal
def resample_signal(signal, original_rate, new_rate):
    """
    Resamples the signal to a new sampling rate.

    Parameters:
        signal (ndarray): Original signal array.
        original_rate (int): Original sampling rate in Hz.
        new_rate (int): New sampling rate in Hz.

    Returns:
        ndarray: Resampled signal array.
    """
    new_length = int(len(signal) * new_rate / original_rate)  # Calculate new length
    return resample(signal, new_length)  # Resample signal

# Plot original and resampled signals
def plot_signals(original_t, original_signal, resampled_signal, new_rate):
    """
    Plots the original and resampled signals.

    Parameters:
        original_t (ndarray): Time array for the original signal.
        original_signal (ndarray): Original signal array.
        resampled_signal (ndarray): Resampled signal array.
        new_rate (int): Sampling rate of the resampled signal in Hz.
    """
    # Generate time array for the resampled signal
    resampled_t = np.linspace(0, original_t[-1], len(resampled_signal))
    
    # Plot both signals
    plt.figure(figsize=(10, 5))
    plt.plot(original_t, original_signal, label="Original Signal", color='blue')
    plt.stem(resampled_t, resampled_signal, linefmt='r-', markerfmt='ro', basefmt=' ',
              label="Resampled Signal")
    plt.title("Original vs Resampled Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()

# Main function to tie it all together
def main():
    """
    Main function to demonstrate signal resampling.
    """
    # Settings
    original_rate = 100  # Hz
    new_rate = 50  # Hz
    frequency = 5  # Hz
    duration = 1  # second
    
    # Generate the original signal
    original_t, original_signal = generate_signal(frequency, original_rate, duration)
    
    # Resample the signal
    resampled_signal = resample_signal(original_signal, original_rate, new_rate)
    
    # Plot the signals
    plot_signals(original_t, original_signal, resampled_signal, new_rate)

# Run the main function
if __name__ == "__main__":
    main()
