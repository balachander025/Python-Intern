import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Load Excel file
df = pd.read_csv("canada_per_capita_income.csv")

# OPTIONAL: Print the first few rows to verify the data
print(df.head())

# Visualize the data
plt.scatter(df.area, df.price, color='red',marker='+')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price')
plt.title('Area vs Price')



# Train the model
reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)

# Predict the price for a 3300 sq ft area
predicted_price = reg.predict([[3300]])
print(f"Predicted price for 3300 sq ft = {predicted_price[0]}")

# Print model parameters
print(f"Coefficient (slope): {reg.coef_[0]}")
print(f"Intercept: {reg.intercept_}")
plt.plot(df.area,reg.predict(df[['area']]),color='blue')
plt.show()
