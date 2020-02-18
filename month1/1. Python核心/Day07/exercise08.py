list1 = [1, 2, 3, 4, 5, 6]
list2 = [(a, b, c) for a in list1 for b in list1 for c in list1]
print(list2)
