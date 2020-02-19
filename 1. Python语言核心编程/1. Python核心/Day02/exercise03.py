minutes = input("分钟：")
hours = input("小时：")
days = input("天数：")
seconds = int(days) * 24 * 60 * 60 + int(hours) * 3600 + int(minutes) * 60
print(days + "天，" + hours + "小时，" + minutes + "分钟，总共是" + str(seconds) + "秒")
