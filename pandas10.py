import pandas as pd


df = pd.DataFrame({
    'Age': [25, 30, 35, 42, 28]
})


def categorize_age(age):
    if age < 30:
        return "Young"
    elif 30 <= age <= 40:
        return "Adult"
    else:
        return "Senior"


df['Category'] = df['Age'].apply(categorize_age)

print(df)
