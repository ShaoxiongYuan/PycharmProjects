list1 = [34, 8, 56, 9, 8, 9]
result = False
for i in range(len(list1) - 1):
    for a in range(i + 1, len(list1)):
        if list1[i] == list1[a]:
            result = True
            break
    if result:
        break

print(result)
