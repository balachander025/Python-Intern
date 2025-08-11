import matplotlib.pyplot as plt 
import numpy as np

a=np.arange(5)
b=[1,2,3,4,5]
c=[2,3,4,5,6]

fig=plt.figure()
ax=plt.subplot()

ax.plot(a,b,'k--',label="frequency")
ax.plot(a,c,'k:',label="period")

legend=ax.legend(loc="upper center")
legend.get_frame().set_facecolor('red')

plt.title("the data")

plt.show()