str_input = input("请输入一个字符串：")
for i in str_input:
    print(ord(i))

while True:
    str_input = input("请输入编码值：")
    if str_input == "":
        break
    else:
        message = chr(int(str_input))
        print(message)
