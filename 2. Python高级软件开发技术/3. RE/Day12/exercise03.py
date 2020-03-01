import re

str_book = """光绪三十四年（1908年），从章太炎先生学习，为“光复会”会员，并与二弟作人译《域外小说集》，期间生活艰难，以校对书稿补贴生活。 [27] 
宣统元年（1909年），《域外小说集》二册出版。
迷茫困顿
宣统元年（1909年）8月，归国，任杭州、浙江两级师范学堂生理学和化学教员兼任日本教员铃木珪寿的植物学翻译。
宣统二年（1910年）8月，任绍兴中学堂教员兼监学。1911年，写个人的第一篇小说文言小说《怀旧》。 [28-30] 
民国元年（1912年），临时政府成立于南京，应教育总长蔡元培之邀，任教育部社会教育司第一科科长。八月任命为教育部佥事。从本年起至1917年，他大量抄古碑，辑录金石碑帖，校对古籍，其中也对佛教思想进行了一定的研究。 [31-32] 
民国六年（1917年）7月7日，因张勋复辟乱作，愤而离职，14日，乱平即返部。 [33] 
画家空行道人李振凯先生笔下的鲁迅
画家空行道人李振凯先生笔下的鲁迅
民国七年（1918年）1月，参加《新青年》改组，任编委。
文坛先声
鲁迅《娜拉走后怎样》演讲
鲁迅《娜拉走后怎样》演讲(2张)
民国七年（1918年）5月，以鲁迅为笔名发表中国现代文学史上第一篇用现代体式创作的白话短篇小说《狂人日记》，载在《新青年》第四卷第五号。 [34-35] 
民国九年（1920年），在北京大学，北京高等师范学校讲授中国小说史，6月，读《共产党宣言》中文译本盛赞译者。9月，发表小说《风波》。 [36-37] 
民国十二年（1923年）8月，小说集《呐喊》出版；与弟弟周作人分居，迁至西四塔胡同61号居住，分居原因不明。12月，作《娜拉走后怎样》演讲，兼任女师大，世界语学校教师；《中国小说史略》上册出版。 [37]  [38] 
民国十三年（1924年）7月，赴西安讲《中国小说的历史变迁》。8月返京。11月，《语丝》周刊出版，鲁迅在首期发表《论雷峰塔的倒掉》，自此鲁迅成为《语丝》作家群的主将之一。"""

print(re.search(r"(\d{1,3}\.){3}\d{1,3}", "IPv4:192.168.0.114").group())
print(re.findall(r"《.+?》", str_book))
print(re.findall(r"\d{4}-\d{1,2}-\d{1,2}", "1984-10-24     1990-5-6     1993-05-03"))
print(re.findall(r"\d{18}[A-Z]*", "身份证号：500106200203123819"))
