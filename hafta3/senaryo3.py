import numpy as np

# Fiyat matrisi
F = np.random.rand(120, 6)

# Günlük getiri
R = np.diff(F, axis=0) / F[:-1]

# Kovaryans matrisi
cov_mat = np.cov(R, rowvar=False)

# Özdeğer ve özvektörler
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

# En küçük özdeğere karşılık gelen özvektör
min_vec = eig_vecs[:, eig_vals.argmin()]
