# 芯片表面瑕疵检测
import cv2
import numpy as np

im = cv2.imread('../data/CPU3.png')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# 二值化处理
ret, im_bin = cv2.threshold(gray, 162, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', im_bin)

# 轮廓提取
img, contours, hierarchy = cv2.findContours(im_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
mask = np.zeros(im_bin.shape, dtype=np.uint8)
mask = cv2.drawContours(mask, contours, -1, (255, 255, 0), -1)
cv2.imshow('mask', mask)

# 相减
im_sub = cv2.subtract(mask, im_bin)
cv2.imshow('im_sub', im_sub)

# 闭运算
k = np.ones((10, 10), np.uint8)
im_close = cv2.morphologyEx(im_sub, cv2.MORPH_CLOSE, k, iterations=3)
cv2.imshow('im_close', im_close)

# 绘制最小外接圆
image, contours, _ = cv2.findContours(im_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
(x, y), radius = cv2.minEnclosingCircle(contours[1])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(im, center, radius, (0, 0, 255), thickness=2)
cv2.imshow('circle', im)

# 计算瑕疵面积
area = np.pi * radius * radius
print('area:', area)
if area > 12:
    print('度盘表面有瑕疵')

cv2.waitKey()
cv2.destroyAllWindows()
