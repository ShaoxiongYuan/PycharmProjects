# 电影推荐项目

## 样本数据集

### 完整电影数据

**m_all_info.csv** 

| 电影id | 电影名称 | 导演 | 编剧 | 主演 | 电影类型 | 上映地区 | 语言 | 上映时间 | 电影时长 | 别名 | 关联ID |
| ------ | -------- | ---- | ---- | ---- | -------- | -------- | ---- | -------- | -------- | ---- | ------ |
|        |          |      |      |      |          |          |      |          |          |      |        |



### 数据二次整理

**m_info.csv**

| 电影id | 演员 | 电影类型 |
| ------ | ---- | -------- |
|        |      |          |

**m_name.csv**

| 电影id | 电影名称 |
| ------ | -------- |
|        |          |

**u_score.csv** 

| 电影id | 用户id | 评分 | 电影类型 |
| ------ | ------ | ---- | -------- |
|        |        |      |          |



## 电影推荐算法 -- 基于物品的协同过滤推荐算法（Item-Based CF）

### 算法思路

1. 加载所有数据。

   ```python
   def init_all_data():
       pass
   ```

1. 整理User对Item的评分矩阵。

   ```python
   def init_user_item_mat():
       """
       加载u_score.csv, 初始化User对Item的评分矩阵。并全局存储。
       """
       pass
   ```

2. 整理Item对Item的相似度矩阵。

   ```python
   def init_item_item_simmat():
       """
       通过导演、演员、电影类型、语言、时间整理item与item的相似度矩阵
       """
       for itemA in items:
           for itemB in items:
               itemA = init_vec_by_itemid(itemA.ID)
               itemB = init_vec_by_itemid(itemB.ID)
       pass
   
   def init_vec_by_itemid(itemId):
       """
       返回itemId电影的特征向量
       导演       演员              电影类型         语言    上映时间
       000001000 0000000101010111 00111011001110  101110  2019
       """
       return [0,1,0,0,0,0,1,1,0...]
   ```

3. 召回算法：每部电影最相似的topN电影。

   ```python
   def sim_items_recall(itemId, topN):
       """
       根据ItemId找到最相似topN个电影
       """
       return [ID1, ID2, ID3...]
   ```

4. 排序算法：使用用户对电影的评分作为权重，为召回的电影列表进行排序。

   ```python
   def items_sort(itemIds, weights):
       """
       计算每部电影的推荐度：电影的平均分 * 电影推荐度权重
       
       itemIds:
       	为当前用户推荐的电影Id列表
       weights:
       	每部推荐的电影的推荐度权重列表
       """
       return sortedIndices
   ```




## 电影推荐算法 -- 基于用户画像的协同过滤推荐算法

### 用户画像

它是根据用户在互联网留下的种种数据，主动或被动地收集，最后加工成一系列的标签。

**用户画像的应用**

精准营销：运营最熟悉的玩法，从粗放式到精细化，将用户群体切割成更细的粒度，辅以短信、推送、邮件、活动等手段，驱以关怀、挽回、激励等策略。

数据应用：用户画像是很多数据产品的基础，诸如耳熟能详的推荐系统广告系统。广告投放基于一系列人口统计相关的标签，性别、年龄、学历、兴趣偏好、手机等等。

用户分析：产品早期，PM们通过用户调研和访谈的形式了解用户。在产品用户量扩大后，调研的效用降低，这时候会辅以用户画像配合研究。新增的用户有什么特征，核心用户的属性是否变化等等。

数据分析：用户画像可以理解为业务层面的数据仓库，各类标签是多维分析的天然要素。数据查询平台会和这些数据打通。

**构建用户画像系统**

1. 以业务为指导，设计合理的用户画像标签体系。
2. 针对画像系统中的每个标签的意义，基于某种机器学习算法为每位用户构建画像标签体系。



### 算法思路

1. 加载所有数据。

   ```python
   def init_all_data():
       pass
   ```

2. 设计用户画像标签。

   ```python
   0,传记,思维清晰
   1,儿童,充满爱心
   2,冒险,好奇心强
   3,剧情,善于思考
   4,动作,热血
   5,动画,保持童心
   6,励志,生活缺少动力
   7,历史,恋旧
   8,古装,内向
   9,同性,突破世俗
   10,喜剧,活泼开朗
   11,奇幻,思维跳跃
   12,家庭,向往温馨
   13,恐怖,心里承受能力强
   14,悬疑,心思缜密
   15,情色,孤单
   16,惊悚,追求刺激
   17,战争,勇猛刚烈
   18,歌舞,追求高雅
   19,武侠,侠肝义胆
   20,灾难,逃避现实
   21,爱情,单纯
   22,犯罪,狂热分子
   23,真人秀,自恋
   24,短片,兴趣广泛
   25,科幻,富有想象力
   26,纪录片,沉稳
   27,脱口秀,喜欢凑热闹
   28,西部,自由奔放
   29,运动,阳光灿烂
   30,音乐,高雅
   31,黑色电影,豪情仗义
   ```

3. 根据每个用户画像标签的特点，为每个用户预测标签体系。

   1. 获取每个用户看过的所有电影及相应的电影类型。
   2. 每种类型对应一种画像标签，统计当前用户的标签体系并存储。tag_table.csv / u_idx.csv

4. 通过用户画像标签体系，构建基于用户的协同过滤算法。整理用户特征向量，基于KMeans训练聚类模型。

   ```python
   def init_user_persona_mat():
       """
       整理用户的画像特征矩阵, 每行为一个用户，每一列为一个标签，每个值为当前用户属于该标签的权重
       """
       persona_mat = []
       for user in users:
       	user_vec = init_uservec_by_id(user.ID)
           persona_mat.append(user_vec)
       # 对persona_mat做行级归一化
       persona_mat = sklearn.preprocessing.normalize(persona_mat)
       # 构建KMeans聚类模型，用于寻找相似用户。
       model = sc.KMeans(n_clusters=20)
       pass
   
   def init_uservec_by_id(user_id):
       """
       加载tag_table.csv与u_idx.csv读取用户画像标签，整理用户特征向量
       返回相应userId用户的特征向量
              0   1   2   3    4
       user:  5.  4.  5.  12.  3.  ....
       """
       return [5., 1., 3., 2., ...] 
   ```

5. 召回算法：基于KMeans模型获取相似用户，通过相似用户获取电影推荐清单。

   ```python
   def sim_users_recall(user_id):
       """
       根据userId找到同类User的id，返回userId列表
       """
       pred_y = model.predict(用户画像特征向量)
       sim_mask = model.labels == pred_y
       return np.where()
   
   def sorted_reclist_recall(user_id, sim_user_ids):
       """
       根据每位相似用户ID，生成电影清单。（不重复）
       基于画像特征向量，计算当前用户与每位用户的欧氏距离得分作为电影推荐度权重 - W
       以 W * 每部电影平均分 作为电影推荐度为列表排序返回itemids
       """
       return [1, 5, 7, 9,...]
   ```





