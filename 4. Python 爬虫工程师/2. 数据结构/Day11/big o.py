import time

start_time = time.time()
# for n1 in range(0, 1001):
#     for n2 in range(0, 1001):
#         for n3 in range(0, 1001):
#             if n1 + n2 + n3 == 1000 and n1 ** 2 + n2 ** 2 == n3 ** 2:
#                 print('[%d,%d,%d]' % (n1, n2, n3))
for n1 in range(0, 501):
    for n2 in range(0, 501):
        n3 = 1000 - n1 - n2
        if n1 ** 2 + n2 ** 2 == n3 ** 2:
            print('[%d,%d,%d]' % (n1, n2, n3))
end_time = time.time()
print('执行时间:%.2f秒' % (end_time - start_time))
