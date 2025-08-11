import pandas as pd
df=pd.read_csv('your.csv')

filtered_df = df[df['Age'] > 30]

print("\n---- Rows where Age > 30 ----")
print(filtered_df)