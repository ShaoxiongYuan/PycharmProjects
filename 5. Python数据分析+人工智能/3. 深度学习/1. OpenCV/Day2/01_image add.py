import cv2

a = cv2.imread('../data/lena.jpg', 0)
b = cv2.imread('../data/lily_square.png', 0)

dst1 = cv2.add(a, b)
dst2 = cv2.addWeighted(a, 0.6, b, 0.4, 0)
dst3=cv2.subtract(a, b)

cv2.imshow('lena', a)
cv2.imshow('lily', b)
cv2.imshow('add', dst1)
cv2.imshow('addweighted', dst2)
cv2.imshow('subtract', dst3)

cv2.waitKey()
cv2.destroyAllWindows()
