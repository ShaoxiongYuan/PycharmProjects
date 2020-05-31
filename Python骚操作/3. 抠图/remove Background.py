import os
import paddlehub as hub

humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')  # 加载模型
path = './images/'  # 文件目录
files = [path + i for i in os.listdir(path)]  # 获取文件列表
results = humanseg.segmentation(data={'image': files})  # 抠图
print(results)
