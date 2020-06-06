from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sn
import warnings

warnings.filterwarnings('ignore')

im = sn.imread('../data/zebra.png', flatten=True)

flt = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]])
flt2 = np.array([[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -1]])

conv_img1 = signal.convolve2d(im, flt, boundary='symm', mode='same')
conv_img2 = signal.convolve2d(im, flt2, boundary='symm', mode='same')

plt.figure("Conv2D")
plt.subplot(131)
plt.xticks([])
plt.yticks([])
plt.imshow(im, cmap='gray')  # 显示原始的图

plt.subplot(132)
plt.xticks([])
plt.yticks([])
plt.imshow(conv_img1, cmap='gray')  # 卷积后的图

plt.subplot(133)
plt.xticks([])
plt.yticks([])
plt.imshow(conv_img2, cmap='gray')  # 卷积后的图

plt.show()
