import cv2
import numpy as np

im = cv2.imread('../data/6.png')
cv2.imshow('im', im)

kernel = np.ones((3, 3), dtype=np.uint8)
dilation = cv2.dilate(im, kernel, iterations=5)

cv2.imshow('dilate', dilation)

cv2.waitKey()
cv2.destroyAllWindows()
