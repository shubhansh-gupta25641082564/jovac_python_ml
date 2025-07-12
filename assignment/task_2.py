import numpy as np
# creating array
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
arr = np.array(data)
first_three = arr[:3]
alternate = arr[::2]
reversed_arr = arr[::-1]
print("Original array:      ", arr)
print("First three elems:   ", first_three)
print("Every alternate elem:", alternate)
print("Reversed array:      ", reversed_arr)