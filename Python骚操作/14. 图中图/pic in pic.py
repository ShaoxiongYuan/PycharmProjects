import os
import cv2
import numpy as np


def getDominant(im):
    """获取主色调"""
    b = int(round(np.mean(im[:, :, 0])))
    g = int(round(np.mean(im[:, :, 1])))
    r = int(round(np.mean(im[:, :, 2])))
    return (b, g, r)


def getColors(path):
    """获取图片列表的色调表"""
    colors = []

    filelist = [path + i for i in os.listdir(path)]
    for file in filelist:
        im = cv2.imdecode(np.fromfile(file, dtype=np.uint8), -1)
        dominant = getDominant(im)
        colors.append(dominant)
    return colors


def fitColor(color1, color2):
    """返回两个颜色之间的差异大小"""
    b = color1[0] - color2[0]
    g = color1[1] - color2[1]
    r = color1[2] - color2[2]
    return abs(b) + abs(g) + abs(r)


def generate(im_path, imgs_path, box_size, multiple=1):
    """生成图片"""

    # 读取图片列表
    img_list = [imgs_path + i for i in os.listdir(imgs_path)]

    # 读取图片
    im = cv2.imread(im_path)
    im = cv2.resize(im, (im.shape[1] * multiple, im.shape[0] * multiple))

    # 获取图片宽高
    width, height = im.shape[1], im.shape[0]

    # 遍历图片像素
    for i in range(height // box_size + 1):
        for j in range(width // box_size + 1):

            # 图块起点坐标
            start_x, start_y = j * box_size, i * box_size

            # 初始化图片块的宽高
            box_w, box_h = box_size, box_size

            box_im = im[start_y:, start_x:]
            if i == height // box_size:
                box_h = box_im.shape[0]
            if j == width // box_size:
                box_w = box_im.shape[1]

            if box_h == 0 or box_w == 0:
                continue

            # 获取主色调
            dominant = getDominant(im[start_y:start_y + box_h, start_x:start_x + box_w])

            img_loc = 0
            # 差异，同主色调最大差异为255*3
            dif = 255 * 3

            # 遍历色调表，查找差异最小的图片
            for index in range(colors.__len__()):
                if fitColor(dominant, colors[index]) < dif:
                    dif = fitColor(dominant, colors[index])
                    img_loc = index

            # 读取差异最小的图片
            box_im = cv2.imdecode(np.fromfile(img_list[img_loc], dtype=np.uint8), -1)

            # 转换成合适的大小
            box_im = cv2.resize(box_im, (box_w, box_h))

            # 铺垫色块
            im[start_y:start_y + box_h, start_x:start_x + box_w] = box_im

            j += box_w
        i += box_h

    return im


if __name__ == '__main__':
    # 获取色调列表
    colors = getColors('./images_style/')
    result_im = generate('download.png', './images_style/', 50, multiple=5)
    cv2.imwrite('result.jpg', result_im)
