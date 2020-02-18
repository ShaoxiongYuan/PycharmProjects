import time


def live_time(year, month, day):
    str_time = "%d-%d-%d" % (year, month, day)
    time_tuple = time.strptime(str_time, "%Y-%m-%d")
    total_second = time.time() - time.mktime(time_tuple)
    d = total_second // (24 * 60 * 60)
    h = total_second % (24 * 60 * 60) // 3600
    m = total_second % (24 * 60 * 60) % 3600 // 60
    s = total_second % (24 * 60 * 60) % 3600 % 60
    return "你活了%d天，%d小时，%d分钟，%d秒" % (d, h, m, s)


print(live_time(1974, 4, 27))
