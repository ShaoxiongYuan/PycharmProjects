start_h = float(input("请输入高度："))
count = 0
dis = start_h
while start_h > 0.01:
    start_h /= 2
    count += 1
    dis += start_h * 2
print(f"{count-1}次")
print("走了%.2fm" % (dis-start_h*2))
