import pandas as pd

df = pd.DataFrame (
    {
        "Name": ["Gabriel Evynhas", "Caio Slapi", "Douglas Zeus"],
        "Age": [21,26,25],
        "Situao": ["Medio", "Pobre", "Rico"],
    }
)

print(df)

print(df["Situao"])

ages = df["Age"]

print(ages.describe())