import numpy as np
import time
A = np.random.random((100, 100))
B = np.random.random((100, 100))
start_time = time.perf_counter()
C = np.dot(A, B)
try:
    det_C = np.linalg.det(C)
except np.linalg.LinAlgError as e:
    det_C = None
    print("Error computing determinant:", e)
try:
    inv_C = np.linalg.inv(C)
except np.linalg.LinAlgError:
    inv_C = None
    print("Matrix is singular; inverse cannot be computed.")
end_time = time.perf_counter()
elapsed = end_time - start_time
print(f"Time taken for multiplication, det, and inv: {elapsed:.6f} seconds")
print("Result matrix C has shape:", C.shape)
if det_C is not None:
    print(f"Determinant of C: {det_C:.6e}")
else:
    print("Determinant: could not be computed.")
if inv_C is not None:
    print("Inverse of C computed successfully.")
else:
    print("Inverse: not available.")