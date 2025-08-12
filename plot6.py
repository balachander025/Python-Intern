import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Start subplot
plt.figure(figsize=(10, 10))

# Line chart
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line")

# Bar chart
plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Bar")

# Scatter plot
plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter")

# Pie chart
plt.subplot(2, 2, 4)
plt.pie([30, 40, 30], labels=["A", "B", "C"])
plt.title("Pie")

# Show all plots
plt.tight_layout()
plt.show()
