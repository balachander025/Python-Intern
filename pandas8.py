import pandas as pd



df = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Age': [25, 30, 22, 28, 26]
})

sorted_df = df.sort_values(by='Age', ascending=False)

print(sorted_df)
