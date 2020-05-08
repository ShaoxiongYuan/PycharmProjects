def bubble_sort(li):
    for j in range(0, len(li) - 1):
        for i in range(0, len(li) - j - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]

    return li


li = [3, 8, 2, 5, 1, 4, 6, 7]
print(bubble_sort(li))
