import numpy as np

# Puanlar
P = np.random.randint(0, 100, (100, 3))

# Sıralama (S3 desc, S1 asc)
idx = np.lexsort((-P[:, 2], P[:, 0]))

# İlk 10 öğrenci
top10 = P[idx[:10]]
