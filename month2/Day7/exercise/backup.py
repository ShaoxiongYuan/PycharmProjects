import os

dir = "/home/tarena/Backup/"

location = input("请输入需要备份的文件夹位置：")
if location[-1] != "/":
    location += "/"


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


def main():
    for item in os.listdir(location):
        if os.path.isfile(location + item):
            copy(item)


if __name__ == '__main__':
    main()
