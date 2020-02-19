def total_seconds(hour=0, minute=0, second=0):
    total = hour * 3600 + minute * 60 + second
    print(total)


total_seconds(1, 2, 3)
total_seconds(1, 2)
total_seconds(minute=2)
total_seconds(1, second=3)
