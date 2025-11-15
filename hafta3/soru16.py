import numpy as np

matris = np.random.randint(0, 100, (5, 5))

ortalama = matris.mean()
max_deger = matris.max()
std_sutun = matris.std(axis=0)

print("Matris:\n", matris)
print("Ortalama:", ortalama)
print("En büyük değer:", max_deger)
print("Sütun bazında standart sapma:", std_sutun)
