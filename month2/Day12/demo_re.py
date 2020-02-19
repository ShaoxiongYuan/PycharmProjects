import re

print(re.findall("ab", "abcdefabcd"))
print(re.findall("中国", "你好，中国"))
print(re.findall("ab|ef", "abcdefabcd"))
print(re.findall("ab|bc", "abcdefabcd"))
print(re.findall("张.丰", "张三丰，张四丰，张五丰"))
print(re.findall("张..", "张三丰，张四丰，张五丰"))
print(re.findall("[abcd]", "abcdefabcd"))
print(re.findall("[a-z]", "How are you"))
print(re.findall("[h0-9]", "h007"))
print(re.findall("[^h0-9]", "h 0 0 7"))
print(re.findall("[^ ]", "h 0 0 7"))
