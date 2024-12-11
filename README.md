# Signal Resampling and Error Analysis

This repository contains two Python applications demonstrating signal resampling techniques and their effects:
1. **`resample_demo.py`**: A simple demo that visualizes the effects of resampling on a sine wave signal.
2. **`resample_with_error.py`**: An extended version that includes error analysis, quantifying the deviation between the original and resampled signals.

## Objective
The goal of these apps is to provide an educational demonstration of:
- Signal generation and resampling.
- The effects of reducing the sampling rate.
- Error analysis to measure the quality of resampling and interpolation.

These apps are designed for learners, researchers, and professionals exploring fundamental concepts in signal processing and data visualization.

## Features
### 1. `resample_demo.py`
- Generates a sine wave signal with customizable frequency, duration, and sampling rate.
- Resamples the signal to a lower sampling rate.
- Visualizes the original and resampled signals for comparison.

### 2. `resample_with_error.py`
- All features from `resample_demo.py`.
- Calculates and visualizes the error (difference) between the original and resampled signals.
- Displays Mean Squared Error (MSE) as a quantitative metric.

## Installation and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Signal-Resampling-Demo.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Signal-Resampling-Demo
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the applications:
   - For the basic demo:
     ```bash
     python resample_demo.py
     ```
   - For the extended version with error analysis:
     ```bash
     python resample_with_error.py
     ```

## Examples
### Original vs. Resampled Signal
The plot compares the original sine wave with the resampled version, showing how resampling affects signal fidelity.

### Error Analysis
The extended app visualizes the difference between the original and resampled signals over time, along with the Mean Squared Error (MSE).

## File Structure
```
Signal-Resampling-Demo/
├── resample_demo.py           # Basic resampling demo
├── resample_with_error.py     # Resampling with error analysis
├── README.md                  # Project documentation
├── requirements.txt           # Required Python libraries
├── LICENSE                    # License for the project
```

## Requirements
- Python 3.x
- Libraries:
  - `numpy`
  - `matplotlib`
  - `scipy`

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## Acknowledgments
This project was created as part of a personal learning journey into signal processing and data visualization using Python. Special thanks to the open-source community for their excellent libraries and tutorials.
