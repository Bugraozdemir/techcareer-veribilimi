import numpy as np

M = np.arange(1, 26).reshape(5, 5)

ikinci_satir = M[1]        # [6, 7, 8, 9, 10]
ucuncu_sutun = M[:, 2]     # [3, 8, 13, 18, 23]

print("İkinci Satır:", ikinci_satir)
print("Üçüncü Sütun:", ucuncu_sutun)
