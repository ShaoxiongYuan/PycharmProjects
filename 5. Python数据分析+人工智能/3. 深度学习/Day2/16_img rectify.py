import cv2
import numpy as np
import imutils

im = cv2.imread('../data/paper.jpg')
cv2.imshow('im', im)

# 预处理
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
dilate = cv2.dilate(blurred, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
# cv2.imshow('dilate', dilate)

# 边沿
edged = cv2.Canny(dilate, 30, 120, apertureSize=3)
# cv2.imshow('edged', edged)

# 轮廓
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
im_cnt = cv2.drawContours(im, cnts, -1, (0, 0, 255), thickness=2)
cv2.imshow('contour', im)

# 多边形拟合
docCnt = None
if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)  # 计算面积作为排序依据
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            docCnt = approx
            break

points = []
for peak in docCnt:
    peak = peak[0]
    # 绘制圆
    cv2.circle(im,  # 绘制图像
               tuple(peak), 5,  # 圆心、半径
               (0, 0, 255), 2)  # 颜色、粗细
    points.append(peak)  # 添加到列表
cv2.imshow('circle', im)

src = np.float32([points[0], points[1], points[2], points[3]])
dst = np.float32([[0, 0], [0, 488], [337, 488], [337, 0]])
m = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(gray.copy(), m, (337, 488))
cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()
