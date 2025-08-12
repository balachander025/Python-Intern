import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]


plt.plot(x, y, color='blue', linewidth=2, marker='o')  


plt.title("Simple Line Chart")        
plt.xlabel("X Axis")                  
plt.ylabel("Y Axis")                  

plt.show()
