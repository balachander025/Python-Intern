import matplotlib.pyplot as plt 
import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([2,3,4,5,6])

plt.pie(b,labels=a,autopct='%1.2f%%')
plt.title("the scores")
plt.show()