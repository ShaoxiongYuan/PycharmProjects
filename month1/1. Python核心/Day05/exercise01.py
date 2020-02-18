list_score = []
while True:
    score = input("请输入成绩：")
    if score == "":
        break
    else:
        list_score.append(int(score))
print("最高分是%d分，最低分是%d分，平均分是%f分。" % (max(list_score), min(list_score), sum(list_score) / len(list_score)))

