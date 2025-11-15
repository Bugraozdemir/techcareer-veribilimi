import numpy as np

# Tensör oluşturma
tensor = np.random.rand(5, 20, 8)

# Her zaman adımı için ortalama
zaman_ort = tensor.mean(axis=(0, 2))

# Tüm değerlerin genel ortalaması
genel_ort = tensor.mean()

# Broadcasting ile çıkarma
yeni_tensor = tensor - genel_ort
