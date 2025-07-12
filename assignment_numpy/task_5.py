import numpy as np
np.random.seed(42)
arr = np.random.randint(10, 51, size=15)
print(arr)
greater_than_25 = arr[arr > 25]
print("Elements greater than 25:")
print(greater_than_25)
replaced = arr.copy()
replaced[replaced < 30] = 0
print("Array with elements < 30 replaced by 0:")
print(replaced)
divisible_by_5_count = np.sum(arr % 5 == 0)
print(f"Number of elements divisible by 5: {divisible_by_5_count}")