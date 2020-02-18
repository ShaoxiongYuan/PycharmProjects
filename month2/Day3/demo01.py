f = open("hello.txt", "r")

# data=f.readline(19)
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)

# while True:
#     data=f.read(1024)
#     if not data:
#         break
#     print(data)

# data = f.readlines(1)
# print(data)

for line in f:
    print(line)

f.close()

f = open("1.jpg", "rb")
f.readlines()
