import pandas as pd
data = {
        "Name":   ["Alice", "Bob",   "Carol", "David", "Eve"],
        "Age":    [20,      22,      19,      21,      20],
        "Gender": ["Female","Male",  "Female","Male",  "Female"],
        "Marks":  [85,      78,      92,      74,      88]
    }
df = pd.DataFrame(data)
print("First two rows:")
print(df.head(2), end="\n\n")
print("Column names:")
print(df.columns.tolist(), end="\n\n")
print("Data types:")
print(df.dtypes, end="\n\n")
print("Summary statistics:")
print(df.describe(include="all"), end="\n\n")
df["Passed"] = df["Marks"] >= 80
print("DataFrame with 'Passed' column:")
print(df)