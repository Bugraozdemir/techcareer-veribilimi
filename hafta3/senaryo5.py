import numpy as np

# Tensör
T = np.random.rand(10, 30, 2)

# Parametre ortalamaları
ort = T.mean(axis=(0, 1))

# Broadcasting için reshape
ort_r = ort.reshape(1, 1, 2)

# Anomali tensörü
anomali = T - ort_r
