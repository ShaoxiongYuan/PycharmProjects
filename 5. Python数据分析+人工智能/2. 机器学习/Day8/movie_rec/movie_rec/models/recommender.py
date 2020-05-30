import pandas as pd
import numpy as np
from datasets import *


# 基于物品的协同过滤推荐算法
class ItemBasedCFModel(object):
    def __init(self):
        pass

    def recommend_by_userid(self, uid):
        """通过用户id，返回推荐列表
        1. 找到用户评分最高的5部电影。
        2. 找到每部电影的10部相似电影。
        3. 为召回电影列表排序。
        """
        itemids = user_item_mat.columns.values
        user_movie_scores = user_item_mat.loc[str(uid)]
        user_favirate_top5_movie_scores = user_movie_scores.sort_values(ascending=False)[:5]
        user_favirate_top5_movieids = user_favirate_top5_movie_scores.index.values
        print('user_favirate_top5_movieids:', user_favirate_top5_movieids)
        reco_movies = {}
        for i, itemid in enumerate(user_favirate_top5_movieids):
            movie_score = user_favirate_top5_movie_scores.values[i]
            movie_list, sim_score = self.sim_items_recall(itemid, 10)
            for i, movie in enumerate(movie_list):
                if movie not in reco_movies.keys():
                    reco_movies[movie] = [[], []]
                reco_movies[movie][0].append(movie_score)
                reco_movies[movie][1].append(sim_score[i])
        print('recall movie list:', list(reco_movies.keys()))
        # 计算加权平均
        sorted_reco_movies = sorted(reco_movies.items(), 
                                    key=lambda x: np.average(x[1][0], weights=x[1][1]), reverse=True)
        final_reco_movie_list = []
        for srm in sorted_reco_movies:
            final_reco_movie_list.append(srm[0])
        print('final_reco_movie_list:', final_reco_movie_list)
        return final_reco_movie_list

    def sim_items_recall(self, itemid, topN):
        """
        根据ItemId找到最相似topN个电影
        """
        index = ITEM_ITEM_SIMMAT.index
        sim_score = ITEM_ITEM_SIMMAT.loc[itemid]
        sorted_index = np.argsort(sim_score)[::-1]
        return index[sorted_index][:topN], sim_score.values[sorted_index][:topN]



class PersonaRecommendModel(object):
    # 用户画像推荐模型

    def recommend_by_userid(self, uid):
        # 基于用户画像生成的用户相似度矩阵 查找uid的相似用户
        # 找到最像的5个用户（记录每个人的相似度评分）  看一下他们每个人评分最高的10部电影（记录每个人为每部电影的打分）
        userids, sim_scores = self.sim_users_recall(uid, 10)
        reco_movies = {}
        for userid, sim_score in zip(userids, sim_scores):
            itemids = user_item_mat.columns.values
            user_movie_scores = user_item_mat.loc[str(userid)]
            user_favirate_top10_movies = user_movie_scores.sort_values(ascending=False)[:5]
            for movieid, movie_score in zip(user_favirate_top10_movies.index, user_favirate_top10_movies):
                if movieid not in reco_movies.keys():
                    reco_movies[movieid] = [[],[]]
                reco_movies[movieid][0].append(movie_score)
                reco_movies[movieid][1].append(sim_score)

        # 计算加权平均
        sorted_reco_movies = sorted(reco_movies.items(), 
                                    key=lambda x: np.average(x[1][0], weights=x[1][1]), reverse=True)
        final_reco_movie_list = []
        for srm in sorted_reco_movies:
            final_reco_movie_list.append(srm[0])
        print('final_reco_movie_list:', final_reco_movie_list)
        return final_reco_movie_list
            

    def sim_users_recall(self, uid, topN):
        """
        根据uid找到最相似topN个用户
        """
        simuser_score = USER_USER_SIMMAT.loc[str(uid)]
        simuser_score = simuser_score.drop(str(uid)) # 删掉自己
        recall_users = simuser_score.sort_values(ascending=False)[:topN]
        return recall_users.index, recall_users.values


if __name__ == '__main__':
    # model = ItemBasedCFModel()
    model = PersonaRecommendModel()
    print(model.recommend_by_userid(0))
