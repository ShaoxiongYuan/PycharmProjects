import cv2
import numpy as np

im = cv2.imread('../data/3.png')
cv2.imshow('im', im)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

arr_cnt = np.array(contours)
# print(arr_cnt.shape)
# for cnt in arr_cnt:
#     print(cnt.shape)
#     for point in cnt:
#         print(point)

im_cnt = cv2.drawContours(im, contours, -1, (0, 0, 255), thickness=2)
cv2.imshow('contours', im_cnt)

cv2.waitKey()
cv2.destroyAllWindows()
