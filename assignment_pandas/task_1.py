import pandas as pd
data = [25, 30, 35, 40, 45]
indices = ['A', 'B', 'C', 'D', 'E']
series = pd.Series(data, index=indices)
print("Series with custom indices:")
print(series, end="\n\n")
first_three = series.iloc[:3]
print("First three elements:")
print(first_three, end="\n\n")
mean_val = series.mean()
median_val = series.median()
std_val = series.std()
print("Series statistics:")
print(f"  Mean   = {mean_val}")
print(f"  Median = {median_val}")
print(f"  Std    = {std_val:.2f}")