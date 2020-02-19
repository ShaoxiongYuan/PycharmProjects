def cp(file1, file2):
    f = open(file1, "rb")
    f2 = open(file2, "wb")
    while True:
        data = f.read(1024)
        if not data:
            break
        f2.write(data)
    f.close()
    f2.close()


cp("1.jpg", "3.jpg")
cp("hello.txt", "hello2.txt")

