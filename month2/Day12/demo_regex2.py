import re

s = "2020年2月19日"
pattern = r"\d+"

# iterable = re.finditer(pattern, s)
# for item in iterable:
#     print(item.group())

print(re.match(pattern, s).group())

print(re.search(pattern, s).group())
