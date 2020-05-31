from PIL import Image

# 读取图片
im = Image.open('original.png')
# 宽高各除 3，获取裁剪后的单张图片大小
width = im.size[0] // 3
height = im.size[1] // 3
# 裁剪图片的左上角坐标
start_x = 0
start_y = 0
# 用于给图片命名
im_name = 1
# 循环裁剪图片
for i in range(3):
    for j in range(3):
        # 裁剪图片并保存
        crop = im.crop((start_x, start_y, start_x + width, start_y + height))
        crop.save(str(im_name) + '.png')
        # 将左上角坐标的 x 轴向右移动
        start_x += width
        im_name += 1
    # 当第一行裁剪完后 x 继续从 0 开始裁剪
    start_x = 0
    # 裁剪第二行
    start_y += height
