import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

inner = np.dot(v1, v2)
outer = np.outer(v1, v2)

print("Nokta ürünü:", inner)
print("Dış ürün:\n", outer)
