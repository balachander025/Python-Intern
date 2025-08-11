import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Age': [25, 30, None, 22, 28]
})


df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)
