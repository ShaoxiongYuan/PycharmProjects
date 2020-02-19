list1=[leap_year for leap_year in range(1970,2051) if
       leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0]
print(list1)