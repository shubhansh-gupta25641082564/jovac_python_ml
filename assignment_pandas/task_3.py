import pandas as pd
data = {
        "Name":   ["Alice", "Bob",   "Carol", "David", "Eve"],
        "Age":    [20,      22,      19,      21,      20],
        "Gender": ["Female","Male",  "Female","Male",  "Female"],
        "Marks":  [85,      78,      92,      74,      88]
    }
df = pd.DataFrame(data)
df["Passed"] = df["Marks"] >= 80
name_marks = df[["Name", "Marks"]]
print("Name and Marks columns:")
print(name_marks, end="\n\n")
high_scorers = df[df["Marks"] > 80]
print("Students with Marks > 80:")
print(high_scorers, end="\n\n")
top_idx = df["Marks"].idxmax()
top_student = df.loc[top_idx]
print("Student with highest marks:")
print(top_student)