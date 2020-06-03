import cv2

im = cv2.imread('../data/Linus.png', 1)
cv2.imshow('BGR', im)

img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray', img_gray)

cv2.waitKey()
cv2.destroyAllWindows()
