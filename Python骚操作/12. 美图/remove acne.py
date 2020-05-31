import cv2

level = 22  # 降噪等级
img = cv2.imread('girl.png')  # 读取原图
img = cv2.bilateralFilter(img, level, level * 2, level / 2)  # 美颜
cv2.imwrite('result.png', img)
