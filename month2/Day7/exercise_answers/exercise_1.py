"""
创建两个进程
分别复制文件的上半部分和下半部分到一个新的文件中
"""

import os

filename = './face.jpg'
size = os.path.getsize(filename)

# 父进程创建fr 两个子进程使用这个fr会相互影响
# fr = open(filename,'rb')

# 复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()

pid = os.fork()
if pid < 0:
	print("Error")
elif pid == 0:
    top()
else:
    bot()


