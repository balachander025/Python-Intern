import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris'],
    'Salary':[30000,4000,6000]
}
df=pd.DataFrame(data)
df['Salary'] = 50000  # You can replace 50000 with any logic or list

# Remove the 'City' column
if 'City' in df.columns:
    df.drop('City', axis=1, inplace=True)