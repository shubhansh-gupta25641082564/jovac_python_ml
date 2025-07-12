import pandas as pd
data = {
        "Name":   ["Alice", "Bob",   "Carol", "David", "Eve"],
        "Age":    [20,      22,      19,      21,      20],
        "Gender": ["Female","Male",  "Female","Male",  "Female"],
        "Marks":  [85,      78,      92,      74,      88]
    }
df = pd.DataFrame(data)
df.loc[1, 'Marks'] = None
df.loc[4, 'Age']   = None
print("DataFrame with missing values:")
print(df, end="\n\n")
print("Missing values by column:")
print(df.isna().sum(), end="\n\n")
mean_marks = df['Marks'].mean(skipna=True)
df['Marks'].fillna(mean_marks, inplace=True)
print(f"Filled missing Marks with mean ({mean_marks:.2f}):")
print(df, end="\n\n")
df_clean = df.dropna(subset=['Age']).reset_index(drop=True)
print("After dropping rows with missing Age:")
print(df_clean)