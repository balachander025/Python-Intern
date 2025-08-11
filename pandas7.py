import pandas as pd



df = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Age': [25, 30, 22, 28, 26]
})


average_age = df.groupby('City')['Age'].mean()

print(average_age)
