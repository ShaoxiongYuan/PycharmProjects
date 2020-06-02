import cv2
import numpy as np

im = cv2.imread('../data/5.png')
cv2.imshow('im', im)

# 腐蚀
kernel = np.ones((3, 3), dtype=np.uint8)
erosion = cv2.erode(im, kernel, iterations=3)

cv2.imshow('erode', erosion)

cv2.waitKey()
cv2.destroyAllWindows()
