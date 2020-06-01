import cv2

im = cv2.imread('../data/Linus.png')
cv2.imshow('im', im)

vertical = cv2.flip(im, 0)
cv2.imshow('vertical', vertical)

horizontal = cv2.flip(im, 1)
cv2.imshow('horizontal', horizontal)

cv2.waitKey()
cv2.destroyAllWindows()
