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

# Calculate the error between original and resampled signals
def calculate_error(original_signal, resampled_signal, original_t, resampled_t):
    """
    Calculates the error between the original and resampled signals.

    Parameters:
        original_signal (ndarray): Original signal array.
        resampled_signal (ndarray): Resampled signal array.
        original_t (ndarray): Time array for the original signal.
        resampled_t (ndarray): Time array for the resampled signal.

    Returns:
        ndarray: Interpolated resampled signal aligned with original time points.
        ndarray: Error values between the original and interpolated signals.
        float: Mean squared error.
    """
    # Interpolate the resampled signal to align with original time points
    interpolated_signal = np.interp(original_t, resampled_t, resampled_signal)

    # Calculate the difference (error) between original and interpolated signals
    error = original_signal - interpolated_signal

    # Calculate the mean squared error (MSE)
    mse = np.mean(error**2)

    return interpolated_signal, error, mse

# Plot original, resampled, and error signals
def plot_signals_and_error(original_t, original_signal, resampled_signal, resampled_t, interpolated_signal, error, mse):
    """
    Plots the original signal, resampled signal, and the error.

    Parameters:
        original_t (ndarray): Time array for the original signal.
        original_signal (ndarray): Original signal array.
        resampled_signal (ndarray): Resampled signal array.
        resampled_t (ndarray): Time array for the resampled signal.
        interpolated_signal (ndarray): Interpolated resampled signal array.
        error (ndarray): Error values between original and interpolated signals.
        mse (float): Mean squared error.
    """
    plt.figure(figsize=(12, 8))

    # Plot original and resampled signals
    plt.subplot(3, 1, 1)
    plt.plot(original_t, original_signal, label="Original Signal", color='blue')
    plt.stem(resampled_t, resampled_signal, linefmt='r-', markerfmt='ro', basefmt=' ',
             label="Resampled Signal")
    plt.title("Original vs Resampled Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()

    # Plot interpolated signal and error
    plt.subplot(3, 1, 2)
    plt.plot(original_t, original_signal, label="Original Signal", color='blue')
    plt.plot(original_t, interpolated_signal, label="Interpolated Signal", linestyle='--', color='green')
    plt.title("Interpolated Resampled Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()

    # Plot error signal
    plt.subplot(3, 1, 3)
    plt.plot(original_t, error, label=f"Error (MSE={mse:.5f})", color='orange')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.title("Error Between Original and Resampled Signals")
    plt.xlabel("Time (s)")
    plt.ylabel("Error")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

# Main function to tie it all together
def main():
    """
    Main function to demonstrate signal resampling with error analysis.
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
    resampled_t = np.linspace(0, duration, len(resampled_signal), endpoint=False)

    # Calculate error
    interpolated_signal, error, mse = calculate_error(original_signal, resampled_signal, original_t, resampled_t)

    # Plot signals and error
    plot_signals_and_error(original_t, original_signal, resampled_signal, resampled_t, interpolated_signal, error, mse)

# Run the main function
if __name__ == "__main__":
    main()
