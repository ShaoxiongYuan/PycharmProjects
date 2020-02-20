import re

portname = input("请输入端口名称：")

f = open("exc.txt")
while True:
    s = ""
    for line in f:
        if line == "\n":
            break
        s += line
    if not s:
        break
    if s.split(" ")[0] == portname:
        data = re.search(r"([0-9a-f]{4}\.){2}[0-9a-f]{4}", s)
        print(data.group())
        break

f.close()
