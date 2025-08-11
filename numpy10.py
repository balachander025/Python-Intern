import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])


dot = np.dot(A, B)

result_at = A @ B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Multiplication using np.dot():")
print(dot)

print("\nMatrix Multiplication using @:")
print(result_at)
