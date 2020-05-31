from PIL import Image
import paddlehub as hub

# 加载模型
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
# 抠图
results = humanseg.segmentation(data={'image': ['original.png']})
# 读取背景图片
bg = Image.open('bg.png')
# 读取原图
im = Image.open('original.png').convert('RGBA')
im.thumbnail((bg.size[1], bg.size[1]))
# 分离通道
r, g, b, a = im.split()
# 将抠好的图片粘贴到背景上
bg.paste(im, (bg.size[0] - bg.size[1], 0), mask=a)
bg.save('result.png')
