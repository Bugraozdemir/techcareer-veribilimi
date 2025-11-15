import numpy as np

veri = np.array([1, 2, 1, 4, 5, 2, 7, 1])

benzersiz, adet = np.unique(veri, return_counts=True)

print("Benzersiz elemanlar:", benzersiz)
print("Tekrar sayıları:", adet)
