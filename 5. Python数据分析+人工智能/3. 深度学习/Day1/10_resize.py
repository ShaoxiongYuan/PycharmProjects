import cv2

im = cv2.imread('../data/Linus.png')

cv2.imshow('image', im)

h, w = im.shape[:2]

dst_size = (int(w / 2), int(h / 2))  # 缩放目标尺寸，宽高均为原来1/2
resized = cv2.resize(im, dst_size)  # 执行缩放
cv2.imshow("reduce", resized)

dst_size = (500, 500)
method = cv2.INTER_NEAREST
resized = cv2.resize(im, dst_size, interpolation=method)
cv2.imshow('Nearest', resized)

method = cv2.INTER_LINEAR
resized = cv2.resize(im, dst_size, interpolation=method)
cv2.imshow('Linear', resized)         

cv2.waitKey()
cv2.destroyAllWindows()
