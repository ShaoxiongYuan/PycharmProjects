"""
新闻分类
"""

####################预处理########################
import os
from multiprocessing import cpu_count
import numpy as np
import paddle
import paddle.fluid as fluid

data_root = '../data/news_classify/'
data_file = 'news_classify_data.txt'
test_file = 'test_list.txt'
train_file = 'train_list.txt'
dict_file = 'dict_txt.txt'

data_file_path = data_root + data_file
dict_file_path = data_root + dict_file
test_file_path = data_root + test_file
train_file_path = data_root + train_file


# 生成字典
def create_dict():
    dict_set = set()
    with open(data_file_path, encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        # 取出标题部分
        title = line.split('_!_')[-1].replace('\n', '')
        for w in title:  # 取出每个字
            dict_set.add(w)

    # 遍历集合，产生编码
    dict_list = []
    i = 0
    for s in dict_set:
        dict_list.append([s, i])
        i += 1

    dict_txt = dict(dict_list)

    end_dict = {'<unk>': i}
    dict_txt.update(end_dict)

    with open(dict_file_path, 'w', encoding='utf-8') as f:
        f.write(str(dict_txt))

    print('字典生成完成。')


create_dict()
