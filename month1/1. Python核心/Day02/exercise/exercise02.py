totals = int(input("总秒数:"))
h = totals // 3600
m = totals % 3600 // 60
s = totals % 3600 % 60
print(f"{h}小时{m}分钟{s}秒")
