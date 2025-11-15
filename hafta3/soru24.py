import numpy as np

C = np.array([[4, 7], [2, 6]])

ters = np.linalg.inv(C)
kontrol = np.dot(C, ters)

print("Ters Matris:\n", ters)
print("Kontrol (C * C^-1):\n", kontrol)
