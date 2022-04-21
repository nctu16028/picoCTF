#!/usr/bin/env python3

import matplotlib.pyplot as plt

img1 = plt.imread("./scrambled1.png")
img2 = plt.imread("./scrambled2.png")

for j in range(img1.shape[1]):
    for i in range(img1.shape[0]):
        for k in range(img1.shape[2]):
            byte1 = int(img1[i, j, k] * 255)
            byte2 = int(img2[i, j, k] * 255)
            img1[i, j, k] = (byte1 + byte2) % 256 / 255.0

plt.axis("off")
plt.imshow(img1)
plt.show()

