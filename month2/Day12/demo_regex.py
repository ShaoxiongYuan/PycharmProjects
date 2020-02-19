import re

s = "Alex:1990 Sunny:1997"

pattern = r"(\w+):(\d+)"
print(re.findall(pattern, s))

regex = re.compile(pattern)
print(regex.findall(s, 0, 13))
