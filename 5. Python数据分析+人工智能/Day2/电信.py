import numpy as np


def loadtxt():
    """
    读取csv文件，返回保存所有数据的ndarray对象。
    """
    rows = []
    with open('CustomerSurvival.csv') as f:
        for line in f.readlines():
            row = line[:-1].split(',')
            rows.append(tuple(row))
    data = np.array(rows, dtype={
        'names': ['index', 'pack_type', 'extra_time', 'extra_flow', 'pack_change',
                  'contract', 'asso_pur', 'group_user', 'use_month', 'loss'],
        'formats': ['i4', 'i4', 'f8', 'f8', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4']})
    return data


data = loadtxt()

# 流失用户与非流失用户占比？
print('-----流失用户与非流失用户占比？----------------------------')
loss_data = data[data['loss'] == 1]
unloss_data = data[data['loss'] == 0]
print('流失用户占比：%.2f' % (len(loss_data) / len(data)))
print('非流失用户占比：%.2f' % (len(unloss_data) / len(data)))

# 有几种套餐类型？
print('-----有几种套餐类型？----------------------------')
pack_types = data['pack_type']
pack_types = set(pack_types)
print(pack_types)

# 三种套餐类型样本数量占比？
print('-----三种套餐类型样本数量占比？----------------------------')
for pack_type in pack_types:
    sub_data = data[data['pack_type'] == pack_type]
    print(pack_type, ': %.2f' % (len(sub_data) / len(data)), end='   ')
    # 统计每种套餐类型的用户中，流失与非流失用户的比例
    loss = len(sub_data[sub_data['loss'] == 1]) / len(sub_data)
    unloss = len(sub_data[sub_data['loss'] == 0]) / len(sub_data)
    print('其中 流失用户占比: %.2f' % loss, '   非流失用户占比: %.2f' % unloss)

# 更改过套餐类型样本数量占比？
print('-----更改过套餐类型样本数量占比？----------------------')
pack_change0 = data[data['pack_change'] == 0]
print('未改过套餐用户占比: %.2f' % (len(pack_change0) / len(data)))
# 统计流失与非流失用户的比例
loss, unloss = len(pack_change0[pack_change0['loss'] == 1]) / len(pack_change0), len(
    pack_change0[pack_change0['loss'] == 0]) / len(pack_change0)
print('其中 流失用户占比: %.2f' % loss, '   非流失用户占比:%.2f' % unloss)

pack_change1 = data[data['pack_change'] == 1]
print('更改过套餐用户占比: %.2f' % (len(pack_change1) / len(data)))
loss, unloss = len(pack_change1[pack_change1['loss'] == 1]) / len(pack_change1), len(
    pack_change1[pack_change1['loss'] == 0]) / len(pack_change1)
print('其中 流失用户占比: %.2f' % loss, '   非流失用户占比: %.2f' % unloss)
