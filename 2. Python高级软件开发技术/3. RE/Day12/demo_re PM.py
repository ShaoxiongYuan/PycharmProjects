import re

# RE转义字符
print(re.findall(r"\d+\.?\d*", "45 1 1.29 "))
print(re.findall(r"\$\d+", "日薪：$100"))

# Greedy/lazy match
print(re.findall(r"ab+?", "abbbbbbbbbbbc"))
print(re.findall(r"ab*?", "abbbbbbbbbbbc"))
print(re.findall(r"ab??", "abbbbbbbbbbbc"))
print(re.findall(r"ab{3,5}?", "abbbbbbbbbbbc"))

# 分组
print(re.search(r"(ab)+", "abababababab").group())

# 捕获组
print(re.search(r"(?P<dog>ab)+", "abababababab").group())
print(re.search(r"(?P<dog>ab)+", "abababababab").group("dog"))
