import numpy as np

matris = np.random.rand(5, 5)

sutun_ort = matris.mean(axis=0)
merkezlenmis = matris - sutun_ort

print("Orijinal Matris:\n", matris)
print("Sütun Ortalamaları:", sutun_ort)
print("Merkezlenmiş Matris:\n", merkezlenmis)
