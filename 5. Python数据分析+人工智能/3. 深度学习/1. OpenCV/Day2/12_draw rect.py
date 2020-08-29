import cv2
import numpy as np

im = cv2.imread('../data/cloud.png', 0)
cv2.imshow('im', im)

ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('binary', binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

x, y, w, h = cv2.boundingRect(contours[0])
print(x, y, w, h)

brcnt = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
result = cv2.drawContours(im, [brcnt], -1, (255, 255, 255), thickness=2)
cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()
