# --- Data Initialization ---

# Input vector with 52 naturally generated numbers.
# In a real-world scenario, this data would be imported from a file (e.g., a CSV).
number_vector = [
    83647, 19283, 43631, 74703, 50715, 29398, 29782, 45389, 60050, 97867,
    14147, 33075, 83823, 76931, 74689, 97620, 77587, 70980, 51162, 58877,
    70514, 99576, 48557, 44028, 45182, 96562, 56673, 88714, 27128, 77851,
    18387, 28624, 12441, 14154, 55701, 55433, 66088, 19591, 68848, 11773,
    80530, 18967, 21820, 94809, 75900, 24724, 27649, 18463, 98708, 26331,
    79067, 86070
]

# Dictionary to store the count of each leading digit (1 through 9).
# It's initialized to zero for all digits.
digit_counters = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

# --- First Digit Analysis ---

# Loop through each number in the input vector.
for number in number_vector:
    # Get the first character of the number by converting it to a string.
    first_digit_str = str(number)[0]
    # Convert the character back to an integer.
    first_digit_int = int(first_digit_str)
    
    # If the digit is a valid key in our counter dictionary (1-9), increment its count.
    if first_digit_int in digit_counters:
        digit_counters[first_digit_int] += 1

# --- Define Benford's Law Proportions ---

# A dictionary holding the expected percentage for each leading digit according to Benford's Law.
benford_law_percentages = {1: 30.1, 2: 17.6, 3: 12.5, 4: 9.7, 5: 7.9, 6: 6.7, 7: 5.8, 8: 5.1, 9: 4.6}

# --- Calculate and Display Proportions ---

# Dictionary to store the found proportions calculated from the input data.
found_proportions = {}
total_numbers = len(number_vector) # Total count of numbers for calculation.

# Loop from 1 to 9 to calculate the percentage for each digit.
for i in range(1, 10):
  # Formula: (count of a specific digit / total number of items) * 100
  found_proportions[i] = (digit_counters[i] / total_numbers) * 100

# --- Print the Results and Compare ---

print("--- Benford's Law Analysis ---")
print("\nExpected Proportions (Benford's Law):")
for i in range(1, 10):
  # Use an f-string to format the output neatly. The :>5 ensures the percentage is right-aligned.
  print(f"Digit {i} -> {benford_law_percentages[i]:>5}%")

print("\nFound Proportions (from data):")
for i in range(1, 10):
  # The :.2f formats the float to have exactly two decimal places for consistency.
  print(f"Digit {i} -> {found_proportions[i]:>5.2f}%")

print("\n--- Significance Analysis ---")
# Define the significance threshold (1%).
significance_threshold = 1.0

# Loop through each digit to check for significant differences.
for i in range(1, 10):
  # Calculate the absolute difference between the found and expected percentages.
  difference = abs(found_proportions[i] - benford_law_percentages[i])
  
  # Check if the difference is greater than the threshold.
  if difference > significance_threshold:
    print(f"WARNING: The proportion for digit '{i}' is significantly different from Benford's Law.")
