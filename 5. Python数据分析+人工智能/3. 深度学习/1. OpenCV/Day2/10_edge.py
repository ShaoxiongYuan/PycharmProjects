import cv2

im = cv2.imread('../data/lily.png', 0)
cv2.imshow('im', im)

sobel = cv2.Sobel(im, cv2.CV_64F, 1, 1, ksize=5)
cv2.imshow('sobel', sobel)

laplacian = cv2.Laplacian(im, cv2.CV_64F, ksize=5)
cv2.imshow('laplacian', laplacian)

canny = cv2.Canny(im, 50, 140)
cv2.imshow('canny', canny)

cv2.waitKey()
cv2.destroyAllWindows()
