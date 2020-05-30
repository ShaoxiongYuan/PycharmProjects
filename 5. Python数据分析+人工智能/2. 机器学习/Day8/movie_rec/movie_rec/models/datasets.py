"""
当前模块提供电影推荐所有资源数据。
"""
import pandas as pd
import numpy as np
import time
import os

MOVIE_DATA_PATH = 'models/data/m_all_info.csv'
MOVIE_DATA_COLUMNS = ['movie_id', 'title', 'director', 'scriptwriter', 'actors', 'genres',
                          'place', 'languages', 'time', 'duration', 'other_names', '_']
RATING_DATA_PATH = 'models/data/u_score.csv' 
RATING_DATA_CLOLUMNS = ['movie_id', 'user_id', 'rating']

ITEM_ITEM_SIMMAT_PATH = 'models/data/ITEM_ITEM_SIMMAT.csv'
USER_USER_SIMMAT_PATH = 'models/data/USER_USER_SIMMAT.csv'

def init_movie_data():
    """加载所有电影数据"""
    data = pd.read_csv(MOVIE_DATA_PATH, names=MOVIE_DATA_COLUMNS,
        sep=r',\s*', engine='python', encoding='utf-8')
    data.drop_duplicates(subset=['movie_id'], keep='first', inplace=True)
    print('Movie Data loaded:', data.shape)
    return data

def init_rating_data():
    """加载电影评分数据"""
    data = pd.read_csv(RATING_DATA_PATH, names=RATING_DATA_CLOLUMNS, usecols=(0, 1, 2))
    print('Rating Data loaded:', data.shape)
    return data


def init_user_item_mat():
    """
    初始化User对Item的评分矩阵。并全局存储。
    """
    # 获取不重复的user_id列表与movie_id列表作为矩阵行索引标签与列索引标签
    unique_movieids = rating_data['movie_id'].unique()
    unique_userids = rating_data['user_id'].unique()
    user_item_mat = pd.DataFrame(
        0, index=unique_userids, columns=unique_movieids)
    # 遍历rating_data中的每一行数据，充实评分矩阵的内容
    for index, row in rating_data.iterrows():
        user_item_mat[row['movie_id']][row['user_id']] = row['rating']
    print('User_item_mat loaded:', user_item_mat.shape)
    return user_item_mat

movie_data = init_movie_data()
rating_data = init_rating_data()
user_item_mat = init_user_item_mat()
ITEM_ITEM_SIMMAT = None
if os.path.exists(ITEM_ITEM_SIMMAT_PATH):
    print('load model ITEM_ITEM_SIMMAT')
    ITEM_ITEM_SIMMAT = pd.read_csv(ITEM_ITEM_SIMMAT_PATH, index_col=0, header=0)
USER_USER_SIMMAT = None
if os.path.exists(USER_USER_SIMMAT_PATH):
    print('load model USER_USER_SIMMAT')
    USER_USER_SIMMAT = pd.read_csv(USER_USER_SIMMAT_PATH, index_col=0, header=0)
