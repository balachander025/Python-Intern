import matplotlib.pyplot as plt
import pandas as pd

data={
    "cricket":['bala','chander','muruga'],
      "cc":[1,2,3]}
dataframe=pd.DataFrame(data)
plt.plot(dataframe["cricket"],dataframe["cc"])
plt.grid()
plt.show()
