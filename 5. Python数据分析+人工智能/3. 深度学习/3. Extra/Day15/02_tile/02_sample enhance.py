"""
瓷砖检测，样本增强
"""
import os
import cv2
import numpy as np
from global_var import *
import matplotlib.pyplot as plt
from math import *


def do_rotate(im, angle, center=None, scale=1.0):
    h, w = im.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(im, M, (w, h))
    return rotated


def remote(img, angle):
    h, w = img.shape[:2]
    h_new = int(w * fabs(sin(radians(angle))) + h * fabs(cos(radians(angle))))
    w_new = int(h * fabs(sin(radians(angle))) + w * fabs(cos(radians(angle))))

    matRotation = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)

    matRotation[0, 2] += (w_new - w) / 2
    matRotation[1, 2] += (h_new - h) / 2

    imgRotation = cv2.warpAffine(img, matRotation, (w_new, h_new), borderValue=(255, 255, 255))

    return imgRotation


def rotate_all():
    dirs = os.listdir(data_root_path)
    for d in dirs:
        dir_path = os.path.join(data_root_path, d)
        if not os.path.isdir(dir_path):
            continue

        sub_dir_path = os.path.join(dir_path, "Imgs")

        imgs = os.listdir(sub_dir_path)
        for img_file in imgs:
            img_full_path = os.path.join(sub_dir_path, img_file)
            im = cv2.imread(img_full_path)

            # 取出文件名
            pos = img_file.find('.')
            name = img_file[0:pos]
            suffix = img_file[pos:]

            # 循环对图像旋转
            for i in range(1, 8):
                img_new = remote(im, 45 * i)
                img_new_name = '%s_rotate_%d%s' % (name, i, suffix)
                cv2.imwrite(os.path.join(sub_dir_path, img_new_name), img_new)
                print('save ok:', os.path.join(sub_dir_path, img_new_name))


if __name__ == '__main__':
    rotate_all()
    print('图像增强完成')
