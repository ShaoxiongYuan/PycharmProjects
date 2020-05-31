import wordcloud, imageio, jieba

# 1、准备文本数据
sentence = "旗木卡卡西，日本漫画《火影忍者》及其衍生作品中的男性角色。火之国木叶隐村的精英上忍，原木叶暗部成员，四代目火影波风水门的弟子，第七班队长，漩涡鸣人、宇智波佐助、春野樱的老师。年仅12岁就成为上忍的天才忍者，后左眼移植宇智波带土的写轮眼，因使用写轮眼复制了上千种忍术而被称为“拷贝忍者”、“写轮眼卡卡西”，其名号响彻各国。"
# 用jieba将句子分词
word = jieba.cut(sentence)
words = " ".join(word)
# 2、生成图片的nd-array，传入图片路径
im = imageio.imread('kakaxi.jpg')
# 3、创建词云对象
wc = wordcloud.WordCloud(width=600, height=800, background_color='white', font_path='MSYH.TTC', mask=im,
                         contour_width=1, contour_color='black')
# 4、通过文本数据生成词云
wc.generate(words)
# 5、保存词云文件
wc.to_file('result.png')
