import numpy as np

dizi = np.random.randn(100)

kirpilmis = np.clip(dizi, -2, 2)

print(kirpilmis)
