person = {}

f = open("talk.txt", "r")

for each_line in f:
    if each_line[0:] != '\n':  # 分行
        (role, line_spoken) = each_line.split(':', 1)  # 分割人物与话语
        if role not in person:
            person[role] = [line_spoken]
        else:
            person[role].append(line_spoken)

f.close()

for name in person:
    with  open(name+'.txt','w') as fw:
        fw.writelines(person[name])

