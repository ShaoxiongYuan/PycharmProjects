import cv2
import numpy as np

o = cv2.imread("../data/6.png")

k = np.ones((3, 3), np.uint8)
r = cv2.morphologyEx(o, cv2.MORPH_GRADIENT, k)

cv2.imshow("original", o)
cv2.imshow("result", r)

cv2.waitKey()
cv2.destroyAllWindows()
