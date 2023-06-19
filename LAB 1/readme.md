# Bank Data Analysis

This code analyzes a dataset containing bank customer information. The dataset is stored in a CSV file.

## Getting Started

To run the code, follow these steps:

1. Make sure you have the `bank.csv`.
2. Execute the code using a Python interpreter.

## Code Description

The code performs the following operations:

1. Reads the contents of the CSV file and stores the header and data.
2. Prints the header without any quotation marks.
3. Calculates the number of married and single customers and prints the results.
4. Prepares a histogram for the age of customers.
   - The age is extracted from the data and stored in a list.
   - The ages are divided into classes of intervals of 10.
   - The count of customers in each age class is calculated.
   - Finally, the histogram is printed, representing the age distribution.

## Function Details

### marital(data)

This function calculates the number of married and single customers in the dataset.

#### Arguments

- `data`: A list of strings representing the customer data.

### prepare_age_histogram(data)

This function prepares a histogram for the age of customers in the dataset.

#### Arguments

- `data`: A list of strings representing the customer data.


