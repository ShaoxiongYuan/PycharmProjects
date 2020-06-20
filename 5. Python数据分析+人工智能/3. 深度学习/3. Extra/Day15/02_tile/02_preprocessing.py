# 人脸（水果）识别示例：数据预处理
import os
from global_var import *

name_data_list = {}


def save_train_test_file(path, name):
    if name not in name_data_list:  # 未在字典中
        img_list = [path]
        name_data_list[name] = img_list  # 存入字典
    else:
        name_data_list[name].append(path)  # 加入


# 获取所有类别保存的文件夹名称
dirs = os.listdir(data_root_path)
for d in dirs:
    full_path = os.path.join(data_root_path, d)
    if os.path.isdir(full_path):
        full_path = os.path.join(full_path, "Imgs")
        imgs = os.listdir(full_path)
        for img in imgs:
            save_train_test_file(os.path.join(full_path, img), d)
    else:
        pass

# 清空数据文件
with open(test_file_path, "w") as f1:
    pass
with open(train_file_path, "w") as f2:
    pass

for name, img_list in name_data_list.items():
    i = 0
    num = len(img_list)
    print("%s: %d张" % (name, num))

    for img in img_list:
        if i % 10 == 0:
            with open(test_file_path, "a") as f:
                line = "%s\t%d\n" % (img, name_dict[name])
                f.write(line)
        else:
            with open(train_file_path, "a") as f:
                line = "%s\t%d\n" % (img, name_dict[name])
                f.write(line)
        i += 1

print('生成数据列表完成！')
