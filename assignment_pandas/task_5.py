import pandas as pd
data = {
        "Name":   ["Alice", "Bob",   "Carol", "David", "Eve"],
        "Age":    [20,      22,      19,      21,      20],
        "Gender": ["Female","Male",  "Female","Male",  "Female"],
        "Marks":  [85,      78,      92,      74,      88]
    }
df = pd.DataFrame(data)
gender_stats = df.groupby("Gender").agg({
        "Age": "mean",
        "Marks": "mean"
    })
print("Mean Age and Marks by Gender:")
print(gender_stats, end="\n\n")
gender_counts = df["Gender"].value_counts()
print("Number of students by Gender:")
print(gender_counts)