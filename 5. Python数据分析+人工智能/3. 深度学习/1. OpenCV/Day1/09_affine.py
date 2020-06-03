import cv2
import numpy as np


def translate(img, x, y):
    """
    图像平移变换
    :param img:原始图像
    :param x: 平移x坐标
    :param y: 平移y坐标
    :return: 仿射变换后的图像数据
    """
    h, w = img.shape[:2]
    # 构建平移矩阵
    m = np.float32([[1, 0, x],
                    [0, 1, y]])

    shifted = cv2.warpAffine(img, m, (w, h))
    return shifted


def rotate(img, angle, center=None, scale=1.0):
    """
    旋转图片
    :param img: 原始图片
    :param angle: 角度
    :param center: 中心
    :param scale: 缩放比例
    :return: 旋转后的图片
    """
    h, w = img.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    # 构建旋转矩阵
    m = cv2.getRotationMatrix2D(center, angle, scale)
    shifted = cv2.warpAffine(img, m, (w, h))
    return shifted


if __name__ == '__main__':
    im = cv2.imread('../data/Linus.png')
    cv2.imshow('im', im)
    # 平移
    shifted = translate(im, -50, 50)
    cv2.imshow('shifted', shifted)

    # 旋转
    rotated = rotate(im, -30, scale=0.5)
    cv2.imshow('rotated', rotated)

    cv2.waitKey()
    cv2.destroyAllWindows()
