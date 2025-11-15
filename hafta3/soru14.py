import numpy as np

dizi = np.array([1, 2, np.nan, 4, 5, np.nan, 7])

nan_sayisi = np.isnan(dizi).sum()

print("NaN Sayısı:", nan_sayisi)
