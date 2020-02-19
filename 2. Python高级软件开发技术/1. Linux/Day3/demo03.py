f = open("hello.txt", "wb", 10)
while True:
    data = input("字符：")
    if not data:
        break
    f.write(data.encode())
