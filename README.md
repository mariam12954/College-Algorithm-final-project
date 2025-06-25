📚 This project was developed as part of a university coursework with 2 of my colleagues.  
👨‍💻 It includes problem-solving tasks using Python to demonstrate algorithmic thinking and clean code structure
  
 # 🧠 Algorithm Tasks – Python Solutions

This repository contains a collection of algorithmic problems solved using Python. Each task is implemented with clean code and includes basic input/output handling and validation. The goal is to practice and demonstrate problem-solving techniques through well-structured Python scripts.

## Contents

- algorithm_tasks/
  - birthday_cake_candles.py – Count the tallest candles on a birthday cake.
  - median_of_two_sorted_arrays.py – Calculate the median of two sorted arrays after merging and sorting.

## Task 1 – Birthday Cake Candles 🎂

Problem Description  
Given a list of candle heights, determine how many candles are the tallest. Additionally, the implementation checks if the candle height array is symmetric (i.e., reads the same forward and backward).

Example

Input: Enter the number of candles: 5 Enter height of candle1: 4 Enter height of candle2: 3 Enter height of candle3: 4 Enter height of candle4: 2 Enter height of candle5: 4

Output: Max height: 4 Number of tallest candles: 3 Is symmetric: False

Concepts Used
- Iteration
- Max value identification
- Counting occurrences
- Symmetry check

## Task 2 – Median of Two Sorted Arrays 📊

Problem Description  
Given two separate arrays of numbers, the program validates their sizes and values, merges them, sorts the combined array, and then finds the median.

Example

-- Calculate the median of two arrays -- The first array: Enter elements separated by spaces: 1 3 5

The second array: Enter elements separated by spaces: 2 4 6

Output: The median is: 3.5

Concepts Used
- Input parsing and validation
- Bubble sort (for educational purposes)
- Median calculation (odd/even cases)
- Loop control with user interaction

Input Constraints
- Each array's length must be between 0 and 1000.
- Total number of elements (combined) must not exceed 2000.
- Each element must be between -10^6 and 10^6.

## How to Run

Make sure you have Python 3 installed. Clone the repo and run the desired script:

python3 birthday_cake_candles.py

or

python3 median_of_two_sorted_arrays.py
