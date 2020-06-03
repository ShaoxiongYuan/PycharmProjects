import cv2

im = cv2.imread('../data/sunrise.jpg')
cv2.imshow('BGR', im)

yuv = cv2.cvtColor(im, cv2.COLOR_BGR2YUV)

yuv[..., 0] = cv2.equalizeHist(yuv[..., 0])

equal_hist = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
cv2.imshow('yuv', equal_hist)

cv2.waitKey()
cv2.destroyAllWindows()
