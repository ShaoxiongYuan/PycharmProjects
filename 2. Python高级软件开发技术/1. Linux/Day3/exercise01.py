while True:
    dictionary = open("dict.txt", "r")
    word = input("请输入单词：")
    if word == "":
        dictionary.close()
        break
    for line in dictionary:
        if word == line.split(" ")[0]:
            print(line)
            break
        elif word < line.split(" ")[0]:
            print("没有该单词")
            break
    dictionary.close()
