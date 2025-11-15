import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

h = np.hstack((a, b))
v = np.vstack((a, b))

print("Hstack:", h)
print("Vstack:\n", v)
