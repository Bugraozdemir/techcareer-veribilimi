import numpy as np

# Veri serisi
d = np.random.rand(1000)

# Gruplar
g1, g2, g3, g4, g5 = np.split(d, [50, 200, 500, 1000])

# %90 persentil
sonuc = np.array([
    np.percentile(g1, 90),
    np.percentile(g2, 90),
    np.percentile(g3, 90),
    np.percentile(g4, 90),
    np.percentile(g5, 90)
])
