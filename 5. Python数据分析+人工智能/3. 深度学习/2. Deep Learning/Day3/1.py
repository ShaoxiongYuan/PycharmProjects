import random


def continuous(target):
    if 0 not in target:
        new_list = sorted(target)
        for i in range(len(new_list) - 1):
            if new_list[i + 1] - new_list[i] != 1:
                return False
        return True
    else:
        new_list = sorted(target)
    new_list = [new_list[i] for i in range(0, len(new_list)) if new_list[i] != 0]
    # print(new_list)
    zero_count = 5 - len(new_list)
    # print('0的个数：', zero_count)
    for i in range(len(new_list) - 1):
        diff = new_list[i + 1] - new_list[i]
        if diff == 0 or diff > zero_count + 1:
            return False
        zero_count = zero_count - (diff - 1)
    return True


if __name__ == '__main__':
    count = 0
    for time in range(100):
        list1 = []
        for num in range(14):
            for k in range(4):
                list1.append(num)

        cards = random.sample(list1, 5)
        # print(cards)
        if continuous(cards):
            count += 1
    print(count / 100)
