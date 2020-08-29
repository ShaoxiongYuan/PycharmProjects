import cv2

im = cv2.imread("../data/cloud.png")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("im", gray)
# 提取图像轮廓
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary,
                                            cv2.RETR_LIST,
                                            cv2.CHAIN_APPROX_NONE)

ellipse = cv2.fitEllipse(contours[0])
cv2.ellipse(im, ellipse, color=(0, 0, 255), thickness=2)  # 绘制椭圆
cv2.imshow("result", im)

cv2.waitKey()
cv2.destroyAllWindows()