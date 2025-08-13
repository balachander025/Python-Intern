import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel("homeprice.csv.xlsx")




reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)


predicted_price = reg.predict([[3300]])
print(f"Predicted price for 3300 sq ft = {predicted_price[0]}")

print(f"Coefficient (slope): {reg.coef_[0]}")
print(f"Intercept: {reg.intercept_}")
plt.plot(df.area,reg.predict(df[['area']]),color='blue')

with open('model_pickle','wb')as f:
    pickle.dump(reg,f)


plt.show()
