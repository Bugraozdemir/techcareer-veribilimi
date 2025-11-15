import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# NaN olan elemanları silme
temiz = arr[~np.isnan(arr)]

# NaN olan elemanları 0 ile değiştirme
degistirilmis = np.nan_to_num(arr, nan=0)

print("Orijinal dizi:", arr)
print("NaN temizlenmiş:", temiz)
print("NaN -> 0:", degistirilmis)
