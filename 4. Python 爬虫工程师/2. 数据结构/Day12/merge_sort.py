"""
归并排序
"""


def merge_sort(li):
    if len(li) == 1:
        return li

    # 第1步：先分
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_li = merge_sort(left)
    right_li = merge_sort(right)

    # 第2步：再合
    print(left_li, right_li)
    return merge(left_li, right_li)


def merge(left_li, right_li):
    result = []
    while len(left_li) > 0 and len(right_li) > 0:
        if left_li[0] <= right_li[0]:
            result.append(left_li.pop(0))
        else:
            result.append(right_li.pop(0))
    result += left_li
    result += right_li
    return result


if __name__ == '__main__':
    li = [1, 8, 3, 5, 4, 6, 7, 2]
    print(merge_sort(li))
