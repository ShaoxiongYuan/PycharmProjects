f = open("hello.txt", "w")
f.write("hello, bitch\n")
f.write("你好，世界\n")
f.writelines(["你好\n", "hello"])

with open("hello.txt", "r") as f:
    print(f.read())
