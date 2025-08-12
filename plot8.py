import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 7]

plt.plot(x, y)
plt.title("Sample Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


plt.savefig("my_plot.png")  

plt.show()
