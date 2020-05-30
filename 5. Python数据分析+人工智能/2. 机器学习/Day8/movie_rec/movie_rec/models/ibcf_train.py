"""
当前模块用于训练item-item相似度矩阵并存储。
"""
import pandas as pd
import numpy as np
import time
import os
from .datasets import *


def init_item_item_simmat():
    t1 = time.time() * 1000
    itemids = user_item_mat.columns
    ITEM_ITEM_SIMMAT = pd.DataFrame(0.0, index=itemids, columns=itemids, dtype='f8')
    # 整理导演字段多标签二值化处理
    movie_data.index = movie_data['movie_id']
    movie_feature_map = pd.get_dummies(movie_data, columns=['director']) 
    print('movie_feature_map:', movie_feature_map.info(), movie_feature_map.shape)
    # 整理演员字段多标签二值化处理
    L = pd.DataFrame(movie_data['actors'].str.split(' / ', expand=True)).fillna('').values
    import sklearn.preprocessing as sp
    mlb = sp.MultiLabelBinarizer()
    res = pd.DataFrame(mlb.fit_transform(L), columns=mlb.classes_, index=movie_data['movie_id'])
    movie_feature_map2 = pd.concat([movie_feature_map, res], axis=1)
    print('res:', res.info(), res.shape)
    print('movie_feature_map2:', movie_feature_map2.info(), movie_feature_map2.shape)
    
    # 整理电影类型字段多标签二值化处理
    G = pd.DataFrame(movie_data['genres'].str.split(' / ', expand=True)).fillna('').values
    import sklearn.preprocessing as sp
    mlb = sp.MultiLabelBinarizer()
    res = pd.DataFrame(mlb.fit_transform(G), columns=mlb.classes_, index=movie_data['movie_id'])
    movie_feature_map3 = pd.concat([movie_feature_map2, res], axis=1)
    
    # 计算相关性系数矩阵
    movie_feature_map3.drop(movie_feature_map3.columns[np.arange(len(MOVIE_DATA_COLUMNS))], axis=1, inplace=True)
    print(movie_feature_map3.shape)
    ITEM_ITEM_SIMMAT = movie_feature_map3.T.corr()
    return ITEM_ITEM_SIMMAT

ITEM_ITEM_SIMMAT = None
if not os.path.exists(ITEM_ITEM_SIMMAT_PATH):
    print('model training...')
    ITEM_ITEM_SIMMAT = init_item_item_simmat()
    ITEM_ITEM_SIMMAT.to_csv(ITEM_ITEM_SIMMAT_PATH)
else :
    print('model is ready.')

    