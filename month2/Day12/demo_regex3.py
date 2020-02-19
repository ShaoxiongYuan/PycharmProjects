import re

pattern = r"(ab)cd(?P<dog>ef)"

regex = re.compile(pattern)

obj = regex.search("abcdefgh")

print(obj.span())  # 位置

print(obj.groupdict())  # 捕获组 字典

print(obj.group())
print(obj.group(1))
print(obj.group(2))
print(obj.group("dog"))
print(obj.groups())

print(obj.lastgroup)
print(obj.lastindex)
print(obj.endpos)

