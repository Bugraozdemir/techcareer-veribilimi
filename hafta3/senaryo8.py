import numpy as np

# Matrisler
A = np.random.rand(5, 10)
B = np.random.rand(5, 10)
C = np.random.rand(10, 10)

# Stacking
T = np.stack([A, B], axis=0)   # (2, 5, 10)

# Çarpılabilir hale getirme: (5, 10, 10)
out = np.matmul(T.transpose(1, 2, 0), C)
