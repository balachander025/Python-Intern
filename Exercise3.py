import pandas as pd 
import numpy as np
from sklearn import linear_model

df=pd.read_csv("home.csv")
print(df)

d=df.bedrooms.median()
print(d)

df.bedrooms=df.bedrooms.fillna(d)
print(df.bedrooms)

reg=linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)

r=reg.coef_
print(r)