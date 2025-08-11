import matplotlib.pyplot as plt 
import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([2,4,5,6,7])

score=[2,4,6,8,10]

plt.scatter(a,score)
plt.scatter(b,score)

plt.xlabel("Team1")
plt.ylabel("Team2")

plt.title("Cricket")

plt.show()