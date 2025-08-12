import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]
y3 = [25, 20, 15, 10, 5, 0]

# Plot multiple lines with labels
plt.plot(x, y1, label='y = x^2', color='blue')
plt.plot(x, y2, label='y = x', color='green')
plt.plot(x, y3, label='y = -x + 25', color='red')

# Add title and axis labels
plt.title("Multiple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Show plot
plt.show()
