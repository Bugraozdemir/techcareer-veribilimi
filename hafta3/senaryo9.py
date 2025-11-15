import numpy as np

# Veri matrisi
M = np.random.rand(20, 5)

# Rasgele 10 NaN
idx = np.random.choice(M.size, 10, replace=False)
M.flat[idx] = np.nan

# Sütun medyanı
med = np.nanmedian(M, axis=0)

# NaN doldurma
M_filled = np.where(np.isnan(M), med, M)
