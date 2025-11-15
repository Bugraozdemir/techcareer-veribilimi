# 📌 Hafta 3 – NumPy Alıştırmaları ve Senaryolar

Bu repo, Python ve **NumPy** kütüphanesi üzerine hazırlanmış çeşitli alıştırmaları ve senaryoları içeren bir çalışma setidir.
Amaç, NumPy’nin temel fonksiyonlarını, dizi manipülasyonlarını, matematiksel işlemlerini ve küçük uygulama senaryolarını pratik ederek öğrenmektir.

---

## 📂 Proje İçeriği

Proje klasöründe iki ana bölüm bulunur:

### **1️⃣ Soru Dosyaları (`soruX.py`)**

Bu dosyalar küçük ve bağımsız NumPy alıştırmalarını içerir.
Örnek içerikler:

* Temel NumPy dizisi oluşturma
* Dizi bölme, birleştirme
* Matematiksel işlemler
* Rastgele sayılarla çalışma
* Matris işlemleri
* Şekil değiştirme (`reshape`, `flatten`, vb.)

Örnek:

```python
import numpy as np

arr = np.arange(10)
print(arr)
```

---

### **2️⃣ Senaryo Dosyaları (`senaryoX.py`)**

Bu dosyalar daha komplike, gerçek hayata yakın küçük uygulamalardır.

Örneğin:

* 2D görüntü üzerinde kernel ile **evrişim (convolution)** işlemi
* Rastgele matrisler üzerinde istatistiksel analiz
* Veri işleme mini uygulamaları

Örnek (senaryo4.py – 3x3 ortalama filtresi):

```python
import numpy as np

img = np.random.rand(20, 20)
kernel = np.ones((3, 3)) / 9

out = np.sum(img[:18, :18] * kernel[0, 0] +
             img[:18, 1:19] * kernel[0, 1] +
             img[:18, 2:20] * kernel[0, 2] +
             img[1:19, :18] * kernel[1, 0] +
             img[1:19, 1:19] * kernel[1, 1] +
             img[1:19, 2:20] * kernel[1, 2] +
             img[2:20, :18] * kernel[2, 0] +
             img[2:20, 1:19] * kernel[2, 1] +
             img[2:20, 2:20] * kernel[2, 2], axis=0)
```

---

## 🚀 Kurulum

Proje bir sanal ortam içerir ancak kendi ortamınızda çalıştırmak isterseniz:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install numpy
```

---

## ▶️ Çalıştırma

Her dosya bağımsızdır.

Örnek:

```bash
python soru5.py
python senaryo3.py
```

---

## 🎯 Amaç

Bu çalışma kapsamında hedeflenen kazanımlar:

* NumPy dizileriyle etkin şekilde çalışmak
* Çok boyutlu diziler üzerinde işlem yapabilmek
* Basit veri işleme ve matematiksel modelleme örneklerini anlamak
* Görüntü işleme (convolution) mantığını kavramak
* İleri Python çalışmalarına temel oluşturmak

---

## 📎 Notlar

* `main.py` boştur, istersen tüm soruları ve senaryoları bir menü ile çalıştıran bir uygulamaya dönüştürebilirsin.
* `.venv` klasörü GitHub’a yüklememelisin. `.gitignore` eklemen önerilir.

Örnek `.gitignore`:

```
.venv/
__pycache__/
```

---

## 📜 Lisans

Bu proje eğitim amaçlıdır. Dilediğin gibi geliştirebilir ve paylaşabilirsin.

---

