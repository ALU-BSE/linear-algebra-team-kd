import pandas as pd
import numpy as np

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Initialization of empty list Ans to store the result
Ans = []
# (300*200 + 500*100) as an example calculation

# This loop calculates the dot product of each row in Prices with Array2
# For example: (300*200 + 500*100) for the first row
for i in range(len(Prices)):
 row_sum = 0
    for j in range(len(Prices[0])):
        # Multiply each element in the current row with corresponding element in Array2
        # and add it to the row sum
        row_sum += Prices[i][j] * Array2[j]
    # Append the total sum for current row to the answer list
    Ans.append(row_sum)
