import numpy as np

# Görüntü
img = np.random.rand(20, 20)

# Kernel
kernel = np.ones((3, 3)) / 9

# Evrişim (20x20 → 18x18)
out = np.sum(img[:18, :18] * kernel[0, 0] +
             img[:18, 1:19] * kernel[0, 1] +
             img[:18, 2:20] * kernel[0, 2] +
             img[1:19, :18] * kernel[1, 0] +
             img[1:19, 1:19] * kernel[1, 1] +
             img[1:19, 2:20] * kernel[1, 2] +
             img[2:20, :18] * kernel[2, 0] +
             img[2:20, 1:19] * kernel[2, 1] +
             img[2:20, 2:20] * kernel[2, 2], axis=0)
