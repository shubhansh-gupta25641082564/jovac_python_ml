import numpy as np
arr1d = np.arange(1, 13)
print(arr1d)
arr2d = arr1d.reshape(4, 3)
print(arr2d)
print("Shape:", arr2d.shape)
arr3d = arr1d.reshape(2, 2, 3)
print(arr3d)
print("Shape:", arr3d.shape)
arr2d_T = arr2d.T
print(arr2d_T)
print("Shape after transpose:", arr2d_T.shape)