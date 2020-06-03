import cv2

im = cv2.imread("../data/opencv2.png")
print(im.shape)
cv2.imshow("im", im)
# 取出蓝色通道，当做单通道图像显示
b = im[:, :, 0]
cv2.imshow("b", b)
print(b.shape)
# 去掉蓝色通道(索引为0的通道)
im[:, :, 0] = 0
cv2.imshow("im-b0", im)
# # 去掉绿色通道(索引为1的通道)
im[:, :, 1] = 0
cv2.imshow("im-b0g0", im)

cv2.waitKey()
cv2.destroyAllWindows()
