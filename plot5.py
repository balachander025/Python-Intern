import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.randint(0, 3, 50)  


plt.scatter(x, y, c=colors)
plt.title("Scatter Plot with Colored Points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
