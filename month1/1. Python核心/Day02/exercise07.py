leap_year = int(input("Please enter a year:"))
print(leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0)
