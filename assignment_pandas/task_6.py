import pandas as pd
data = {
        "Name":   ["Alice", "Bob",   "Carol", "David", "Eve"],
        "Age":    [20,      22,      19,      21,      20],
        "Gender": ["Female","Male",  "Female","Male",  "Female"],
        "Marks":  [85,      78,      92,      74,      88]
    }
df = pd.DataFrame(data)
df.loc[1, 'Marks'] = None  # Bob's Marks → NaN
df.loc[4, 'Age']   = None  # Eve's Age   → NaN
mean_marks = df['Marks'].mean(skipna=True)
df['Marks'].fillna(mean_marks, inplace=True)
df_clean = df.dropna(subset=['Age']).reset_index(drop=True)
df_clean.to_csv('students_data.csv', index=False)
print("Saved modified DataFrame to 'students_data.csv'.")
df_loaded = pd.read_csv('students_data.csv')
print("\nFirst five rows of the newly loaded DataFrame:")
print(df_loaded.head())