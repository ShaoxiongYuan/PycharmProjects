list1 = [34, 8, 56, 9, 8, 9]
for i in range(len(list1) - 1, -1, -1):
    for a in range(i):
        if list1[i] == list1[a]:
            del list1[i]
            break

print(list1)
