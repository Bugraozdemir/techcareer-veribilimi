import numpy as np

# Noktalar ve referans noktası
A = np.random.rand(50, 4)
B = np.random.rand(1, 4)

# Öklid uzaklıkları
mesafeler = np.sqrt(((A - B) ** 2).sum(axis=1))

# En kısa mesafenin indeksi
en_yakin_indeks = mesafeler.argmin()
