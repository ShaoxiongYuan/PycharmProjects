import cv2

im = cv2.imread('../data/cloud.png', 0)
cv2.imshow('im', im)
# 提取图像轮廓
ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST,
                                            cv2.CHAIN_APPROX_NONE)

(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(im, center, radius, (255, 255, 255), thickness=2)
cv2.imshow('result',im)

cv2.waitKey()
cv2.destroyAllWindows()
