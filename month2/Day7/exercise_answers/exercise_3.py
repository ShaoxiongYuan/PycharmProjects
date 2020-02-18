import os

DIR = "/home/tarena/备份/"
dir = input(">>")
if dir[-1] != '/':
    dir += '/'

def copy(file):
    fr = open(dir+file,'rb')
    fw = open(DIR+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


def main():
    file_list = os.listdir(dir)
    for file in file_list:
        if os.path.isfile(dir+file):
            copy(file)

if __name__ == '__main__':
    main()