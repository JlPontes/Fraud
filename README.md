# Benford's Law Anomaly Detector

A simple Python script to analyze a set of numbers for anomalies by comparing their first-digit distribution against the predictions of Benford's Law.

## About The Project

This project provides a straightforward implementation of Benford's Law, a statistical observation that in many real-life sets of numerical data, the first digit is more likely to be small. Deviations from this pattern can indicate data fabrication, errors, or fraud.

This script analyzes a hardcoded list of 52 numbers to see how well they conform to the expected distribution.

### Benford's Law Expected Distribution

| Digit | Expected Proportion |
| :---: | :-----------------: |
|   1   |        30.1%        |
|   2   |        17.6%        |
|   3   |        12.5%        |
|   4   |        9.7%         |
|   5   |        7.9%         |
|   6   |        6.7%         |
|   7   |        5.8%         |
|   8   |        5.1%         |
|   9   |        4.6%         |

## How It Works

The script performs the following steps:
1.  **Counts Digits**: It iterates through a predefined list of numbers. For each number, it identifies the most significant (first) digit and increments a counter for that digit.
2.  **Calculates Proportions**: It calculates the percentage proportion of each leading digit found in the data.
3.  **Compares to Benford's Law**: It compares the found proportions against the expected proportions defined by Benford's Law.
4.  **Flags Anomalies**: The script identifies a "significant difference" if the found proportion for a digit differs from the expected proportion by more than 1%. It then prints a warning for each such case.

## Getting Started

To run this project, you just need Python 3 installed.

### Installation

1. Clone the repository:
   ```sh
   git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repository-name
   ```

### Running the Script

Execute the Python script from your terminal.

```sh
python analysis.py
```
*(Assuming you name the file `analysis.py`)*

## Example Output

When you run the script, you will get the following output, showing the analysis of the data provided in the code:

```
--- Benford's Law Analysis ---

Expected Proportions (Benford's Law):
Digit 1 ->  30.1%
Digit 2 ->  17.6%
Digit 3 ->  12.5%
Digit 4 ->   9.7%
Digit 5 ->   7.9%
Digit 6 ->   6.7%
Digit 7 ->   5.8%
Digit 8 ->   5.1%
Digit 9 ->   4.6%

Found Proportions (from data):
Digit 1 ->  17.31%
Digit 2 ->  15.38%
Digit 3 ->   1.92%
Digit 4 ->   9.62%
Digit 5 ->  11.54%
Digit 6 ->   5.77%
Digit 7 ->  17.31%
Digit 8 ->   9.62%
Digit 9 ->  11.54%

--- Significance Analysis ---
WARNING: The proportion for digit '1' is significantly different from Benford's Law.
WARNING: The proportion for digit '2' is significantly different from Benford's Law.
WARNING: The proportion for digit '3' is significantly different from Benford's Law.
WARNING: The proportion for digit '5' is significantly different from Benford's Law.
WARNING: The proportion for digit '7' is significantly different from Benford's Law.
WARNING: The proportion for digit '8' is significantly different from Benford's Law.
WARNING: The proportion for digit '9' is significantly different from Benford's Law.
```
