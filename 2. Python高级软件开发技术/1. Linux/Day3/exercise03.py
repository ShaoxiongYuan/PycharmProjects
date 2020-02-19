import time

s = time.localtime()
time_str = time.strftime("%Y.%m.%d %H:%M:%S", s)

f = open("time.txt", "a+")
f.seek(0, 0)
count = 0
for line in f:
    count += 1
while True:
    f.write(str(count + 1) + " ")
    f.write(time_str + "\n")
    f.flush()
    time.sleep(2)
    count += 1
