import os
from threading import Thread

location = input("请输入需要拷贝的文件夹位置：")
if location[-1] != "/":
    location += "/"

dir = input("请输入需要拷贝到的位置：")
os.mkdir(dir)
if dir[-1] != "/":
    dir += "/"


def copy(file):
    f = open(location + file, "rb")
    f2 = open(dir + file, "wb")
    while True:
        data = f.read(1024)
        if not data:
            break
        f2.write(data)
    f.close()
    f2.close()


list_items = os.listdir(location)


def main():
    jobs = []
    for item in list_items:
        if os.path.isfile(location + item):
            t = Thread(target=copy, kwargs={"file": item})
            jobs.append(t)
            t.start()
    for t in jobs:
        t.join()


if __name__ == '__main__':
    main()
