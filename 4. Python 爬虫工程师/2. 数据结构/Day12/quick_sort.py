"""
快速排序
"""


def quick_sort(li, first, last):
    if first > last:
        return

    # 找到基准值正确位置
    mid_index = get_index(li, first, last)

    quick_sort(li, first, mid_index - 1)
    quick_sort(li, mid_index + 1, last)


def get_index(li, first, last):
    mid = li[first]
    lcur = first + 1
    rcur = last
    sign = False

    while not sign:
        while lcur <= rcur and li[lcur] <= mid:
            lcur += 1

        while rcur >= lcur and li[rcur] >= mid:
            rcur -= 1

        if lcur > rcur:
            sign = True
            li[first], li[rcur] = li[rcur], li[first]
        else:
            li[lcur], li[rcur] = li[rcur], li[lcur]

    return rcur


if __name__ == '__main__':
    li = [8, 1, 3, 5, 4, 6, 7, 2, 666, 333]
    quick_sort(li, 0, len(li) - 1)
    print(li)
