import os


def separate_large_files(file):
    size = os.path.getsize(file)

    pid = os.fork()

    if pid < 0:
        print("error")
    elif pid == 0:
        f = open(file)
        file1 = open("1.txt", "w")
        data = f.read(size//2)
        file1.write(data)
    else:
        f = open(file)
        file2 = open("2.txt", "w")
        f.seek(size//2)
        data = f.read()
        file2.write(data)


separate_large_files("new.txt")
