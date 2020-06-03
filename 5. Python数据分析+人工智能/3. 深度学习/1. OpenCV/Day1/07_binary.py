import cv2

im = cv2.imread('../data/lena.jpg', 0)
cv2.imshow('im', im)

t, rst = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', rst)

t, rst = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('inverse binary', rst)

cv2.waitKey()
cv2.destroyAllWindows()
