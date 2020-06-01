"""
图像读取，显示，保存
"""
import cv2

im = cv2.imread('../data/Linus.png', 0)
cv2.imshow('test', im)

print(type(im))
print(im.shape)

cv2.imwrite('Linus_new.png', im)
cv2.waitKey()
cv2.destroyAllWindows()
