import cv2
import numpy as np

im = cv2.imread('../data/pers.png')

rows, cols = im.shape[:2]
print(rows, cols)

# 定义顶点间的映射关系
pts1 = np.float32([[58, 2], [167, 9], [8, 196], [126, 196]])
pts2 = np.float32([[16, 2], [167, 8], [8, 196], [169, 196]])

m = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(im, m, (cols, rows))

m = cv2.getPerspectiveTransform(pts2, pts1)
dst2 = cv2.warpPerspective(dst, m, (cols, rows))

cv2.imshow('im', im)
cv2.imshow('perspective', dst)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()
