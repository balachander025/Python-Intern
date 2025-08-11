import matplotlib.pyplot as plt 
import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,10])
plt.hist(a,bins=[0, 3, 6, 9, 12])

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("The Marks")

plt.show()
