import cv2
import numpy as np

im1 = cv2.imread('../data/9.png')
im2 = cv2.imread('../data/10.png')

k = np.ones((8, 8), dtype=np.uint8)

r1 = cv2.morphologyEx(im1, cv2.MORPH_CLOSE, k, iterations=2)
r2 = cv2.morphologyEx(im2, cv2.MORPH_CLOSE, k, iterations=2)

cv2.imshow('im1', im1)
cv2.imshow('im2', im2)
cv2.imshow('r1', r1)
cv2.imshow('r2', r2)

cv2.waitKey()
cv2.destroyAllWindows()
