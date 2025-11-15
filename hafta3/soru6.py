import numpy as np

arr = np.arange(20)
yeni = arr[(arr > 5) & (arr < 15)]
print(yeni)
