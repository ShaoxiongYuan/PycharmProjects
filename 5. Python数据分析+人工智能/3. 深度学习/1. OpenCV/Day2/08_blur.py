import cv2
import numpy as np

im = cv2.imread('../data/lena.jpg', 0)
cv2.imshow('im', im)

median_blur = cv2.medianBlur(im, 5)
cv2.imshow('median', median_blur)

mean_blur = cv2.blur(im, (3, 3))
cv2.imshow('mean', mean_blur)

gaussian_blur = cv2.GaussianBlur(im, (3, 3), 3)
cv2.imshow('gaussian', gaussian_blur)

gaussian_blur = np.array([
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1, 4, 7, 4, 1]], np.float32) / 273
# 使用filter2D, 第二个参数为目标图像的所需深度, -1表示和原图像相同
im_gaussian_blur2 = cv2.filter2D(im, -1, gaussian_blur)
cv2.imshow("gaussian_blur2", im_gaussian_blur2)

cv2.waitKey()
cv2.destroyAllWindows()
