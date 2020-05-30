1. 模块名改为：movie_recommender
2. 模块中包含类：CommonRecommendModel （普通推荐模型（略））
                            PersonaRecommendModel （基于用户画像的推荐模型）


movie_recommender.py 


def init_common_similarity_matrics():
    # 初始化普通推荐模型的相似用户矩阵
    ...
    return M

def init_persona_similarity_matrics():
    # 初始化基于用户画像推荐模型的相似用户矩阵
    ...
    return M


class CommonRecommendModel (object):
    # 普通推荐模型    
    data = init_common_similarity_matrics()
    def recommend(mtypes):
        # 传入喜欢的电影类型，根据data给出推荐结果
        return [电影id1, 电影id2, 电影id3 ....]

class PersonaRecommendModel (object):
    # 用户画像推荐模型
    data = init_persona_similarity_matrics()
    def recommend(persona_tags):
        # 传入用户画像标签列表，根据data给出推荐结果
        return [电影id1, 电影id2, 电影id3 ....]





请求方式： get
请求路径： http://127.0.0.1:6666/mr/persona/userid/0
                  （最后一部分为当前用户的id）
请求参数：（无）
请求结果： 返回使用用户画像算法针对当前用户的电影推荐id列表，格式如下：
    正常返回：{'status':200, 'data':[1022, 2221,  2321,  4321,  1232], 'msg': null}
    异常返回：{'status':201, 'data':null, 'msg':'异常错误信息提示文本'}
    