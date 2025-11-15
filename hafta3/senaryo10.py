import numpy as np

# Matrisler
A = np.random.rand(10, 3)
B = np.random.rand(10, 3)

# Birleştirme
Y = np.column_stack([A[:, 0], B[:, 1], A[:, 2]])

# Sonuç vektörü
res = np.array([
    np.median(Y[:, 0]),
    np.std(Y[:, 1]),
    np.sum(Y[:, 2])
])
