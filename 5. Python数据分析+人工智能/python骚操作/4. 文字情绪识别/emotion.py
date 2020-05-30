import paddlehub as hub

senta = hub.Module(name='senta_lstm')  # 加载模型
sentence = [  # 准备要识别的语句
    '你真美', '你真丑', '我好难过', '我不开心', '这个游戏好好玩', '什么垃圾游戏',
]
results = senta.sentiment_classify(data={"text": sentence})  # 情绪识别
# 输出识别结果
for result in results:
    print(result)
