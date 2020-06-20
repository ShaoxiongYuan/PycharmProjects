"""
使用OpenCV进行胶囊检测
"""
import cv2 as cv
import numpy as np
import os


def bub_check(img_path, img_file, im, im_gray):
    # 二值化
    ret, im_bin = cv.threshold(im_gray, 180, 255, cv.THRESH_BINARY)
    cv.imshow('im_bin', im_bin)

    # 图像腐蚀
    # kernel = np.ones((3, 3), np.uint8)
    # erosion = cv.erode(im_bin, kernel, iterations=5)
    # cv.imshow('erosion', erosion)

    # 检测边沿
    im_canny = cv.Canny(im_gray, 80, 50)
    cv.imshow('im_canny', im_canny)

    # 提取轮廓
    img, cnts, hir = cv.findContours(im_bin, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    new_acnts = []
    # 计算面积
    for cnt in cnts:
        area = cv.contourArea(cnt)
        # print('area:', area)
        if 20 < area < 10000:
            new_acnts.append(cnt)

    # 绘制轮廓
    im_cnt = cv.drawContours(im, new_acnts, -1, (0, 0, 255), thickness=2)
    cv.imshow('im_cnt', im_cnt)
    if len(new_acnts) > 0:
        print('图像存在气泡瑕疵：', img_path)


def balance_check(img_path, img_file, im, im_gray):
    im_blur = cv.GaussianBlur(im_gray, (5, 5), 0)

    # 膨胀
    im_dilate = cv.dilate(im_blur,
                          cv.getStructuringElement(cv.MORPH_RECT, (5, 5)))
    cv.imshow("dilate", im_dilate)

    # Canny边沿提取
    im_canny = cv.Canny(im_dilate, 60, 200)
    cv.imshow('Canny', im_canny)

    # 提取轮廓
    img, contours, hierarchy = cv.findContours(im_canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    # 计算轮廓面积，过滤掉面积过大的轮廓
    cnts = np.array(contours)
    new_cnts = []

    if len(contours) > 0:
        for cnt in cnts:
            circle_len = cv.arcLength(cnt, True)  # 计算周长
            if circle_len >= 1000:  # 周长太小的过滤掉
                # print("circle_len:", circle_len)
                new_cnts.append(cnt)
    # print(len(new_cnts))

    # 对轮廓排序
    new_cnts = sorted(new_cnts, key=cv.contourArea, reverse=True)
    new_cnts = new_cnts[1:2]
    # print("new_cnts.shape:", np.array(new_cnts).shape)

    # 寻找轮廓中min_x, max_x, min_y, max_y
    max_x, max_y = new_cnts[0][0][0][0], new_cnts[0][0][0][1]
    min_x, min_y = max_x, max_y
    for cnt in new_cnts[0]:
        if cnt[0][0] >= max_x:
            max_x = cnt[0][0]
        if cnt[0][0] <= min_x:
            min_x = cnt[0][0]
        if cnt[0][1] >= max_y:
            max_y = cnt[0][1]
        if cnt[0][1] <= min_y:
            min_y = cnt[0][1]
    print(" min_x:", min_x, " min_y:", min_y, "max_x:", max_x, " max_y:", max_y)

    # cv.line(im, (min_x, min_y), (max_x, min_y), (0, 0, 255), 2)
    # cv.line(im, (min_x, max_y), (max_x, max_y), (0, 0, 255), 2)
    # cv.line(im, (min_x, min_y), (min_x, max_y), (0, 0, 255), 2)
    # cv.line(im, (max_x, max_y), (max_x, min_y), (0, 0, 255), 2)

    # 绘制过滤后的轮廓
    im_cnt = cv.drawContours(im, new_cnts, -1, (0, 0, 255), thickness=2)
    cv.imshow('im_cnt', im_cnt)

    # 计算绘制水平中线
    mid_y = int((min_y + max_y) / 2)
    cv.line(im, (min_x, mid_y), (max_x, mid_y), (0, 0, 255), 2)

    # 计算上半部分水平中线
    mid_up = int((mid_y + min_y) / 2)  # 上半部分中线
    mid_down = int((mid_y + max_y) / 2)  # 下半部分中线
    cv.line(im, (min_x, mid_up), (max_x, mid_up), (0, 0, 255), 2)
    cv.line(im, (min_x, mid_down), (max_x, mid_down), (0, 0, 255), 2)
    cv.imshow("im_line", im)

    # 找中线
    cross_point_up = set()
    cross_point_down = set()
    for cnt in new_cnts[0]:
        x, y = cnt[0][0], cnt[0][1]
        if y == mid_up:
            cross_point_up.add((x, y))
        if y == mid_down:
            cross_point_down.add((x, y))

    cross_point_up = list(cross_point_up)
    cross_point_down = list(cross_point_down)

    for p in cross_point_up:
        cv.circle(im, (p[0], p[1]), 8, (0, 0, 255), 2)
    for p in cross_point_down:
        cv.circle(im, (p[0], p[1]), 8, (0, 0, 255), 2)
    cv.imshow('im_circle', im)

    # 计算上半部分中线，下半部分中线的长度
    len_up = abs(cross_point_up[0][0] - cross_point_up[1][0])
    len_down = abs(cross_point_down[0][0] - cross_point_down[1][0])

    if abs(len_up - len_down) > 8:
        print('大小头瑕疵:', img_path)


if __name__ == '__main__':
    img_dir = '../data/capsules'
    img_files = os.listdir(img_dir)

    for img_file in img_files:
        img_path = os.path.join(img_dir, img_file)
        if os.path.isdir(img_path):
            continue
        else:
            im = cv.imread(img_path, 1)
            im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
            cv.imshow('im', im)
            cv.imshow('im_gray', im_gray)
            # bub_check(img_path, img_file, im, im_gray)
            balance_check(img_path, img_file, im, im_gray)
            cv.waitKey()
            cv.destroyAllWindows()
