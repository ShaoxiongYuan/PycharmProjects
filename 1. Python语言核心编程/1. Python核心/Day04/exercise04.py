sum_value = 0
for i in range(10, 81):
    if i % 10 == 3 or i % 10 == 5 or i % 10 == 9:
        continue
    sum_value += i
print(sum_value)
