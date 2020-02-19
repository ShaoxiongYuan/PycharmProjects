import time


def calculate_week(year, month, day):
    str_time = "%d-%d-%d" % (year, month, day)
    time_tuple = time.strptime(str_time, "%Y-%m-%d")
    index = time_tuple[6]
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week[index]


print(calculate_week(2020, 1, 16))
