import re

print(re.findall("[_A-Za-z0-9]{8,12}", "密码：6546_5Mmao"))

print(re.findall("-?[0-9]+%?", "23, -9 67%"))

print(re.findall("[A-Z]+[a-z]*", "Hello NBA I"))
