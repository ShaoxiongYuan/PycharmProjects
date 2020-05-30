"""
当前模块用于训练user-user相似度矩阵并存储。
"""
import pandas as pd
import numpy as np
import time
import os
from datasets import *

PERSONA_TAG_TABLE_PATH = 'models/terdata/user_tag.csv'
USER_INDEX_PATH = 'models/terdata/u_idx.csv'

def init_user_user_simmat():
    # 加载用户索引与id信息
    users = pd.read_csv(USER_INDEX_PATH, index_col=0, header=None)
    # 加载用户标签信息
    tag_table = pd.read_csv(PERSONA_TAG_TABLE_PATH, header=0)
    # 合并两张表
    user_tag_table = pd.merge(users, tag_table, left_index=True, right_index=True)
    user_tag_table.index = user_tag_table[1]
    del(user_tag_table[1])
    USER_USER_SIMMAT = user_tag_table.T.corr()
    return USER_USER_SIMMAT

if not os.path.exists(USER_USER_SIMMAT_PATH):
    print('UBCF model training...')
    USER_USER_SIMMAT = init_user_user_simmat()
    USER_USER_SIMMAT.to_csv(USER_USER_SIMMAT_PATH)
else :
    print('model is ready.')

    