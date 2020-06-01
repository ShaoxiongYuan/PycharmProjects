from cv2 import *
import numpy as np

im = imread("../data/opencv2.png")
hsv = cvtColor(im, cv2.COLOR_BGR2HSV)
imshow('opencv', im)

# 蓝色
minBlue = np.array([110, 50, 50])
maxBlue = np.array([130, 255, 255])
mask = inRange(hsv, minBlue, maxBlue)
# imshow("mask_blue", mask)

blue = bitwise_and(im, im, mask=mask)
imshow('blue', blue)

# 红色
minRed = np.array([0, 50, 50])
maxRed = np.array([30, 255, 255])
mask = inRange(hsv, minRed, maxRed)
# imshow("mask_red", mask)

red = bitwise_and(im, im, mask=mask)
imshow('red', red)

# 绿色
minGreen = np.array([50, 50, 50])
maxGreen = np.array([70, 255, 255])

mask = inRange(hsv, minGreen, maxGreen)

green = bitwise_and(im, im, mask=mask) # 执行掩模运算
imshow('green', green)

waitKey()
destroyAllWindows()
