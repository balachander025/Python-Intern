import matplotlib.pyplot as plt
import pandas as pd

data={
    "cricket":['bala','chander','muruga'],
      "cc":[1,2,3]}
dataframe=pd.DataFrame(data)
plt.plot(dataframe["cc"],dataframe["cricket"])
plt.show()
