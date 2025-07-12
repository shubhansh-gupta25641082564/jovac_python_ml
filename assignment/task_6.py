import numpy as np
linear_space = np.linspace(0, 1, 10)
identity_mat = np.eye(4)
np.random.seed(0)
rand_ints = np.random.randint(1, 101, size=20)
sorted_ints = np.sort(rand_ints)
largest_five = sorted_ints[-5:]
print(linear_space, "\n")
print(identity_mat, "\n")
print(sorted_ints)
print("   5 largest elements:", largest_five)