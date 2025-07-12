import numpy as np
# 1D array
arr1d = np.arange(1, 11)
# 2D array
arr2d = arr1d[:9].reshape((3, 3))
# 3D array
arr3d = np.random.random((3, 5, 3))
# display function
def show_info(name, arr):
    print(f"{name}:")
    print("  Array:\n", arr)
    print("  Shape   :", arr.shape)
    print("  Size    :", arr.size)
    print("  Datatype:", arr.dtype)
    print("-" * 40)
show_info("1D Array", arr1d)
show_info("2D Array", arr2d)
show_info("3D Array", arr3d)