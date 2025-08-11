import numpy as np


matrix = np.arange(1, 26).reshape(5, 5)

print(matrix)


first_row = matrix[0, :]
print("\nFirst row:")
print(first_row)


last_column = matrix[:, -1]
print("\nLast column:")
print(last_column)


middle_block = matrix[1:4, 1:4]
print("\nMiddle 3x3 block:")
print(middle_block)
