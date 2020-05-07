import re

# pattern = re.compile(r'.', re.S)
# print(pattern.findall('adnaoed2312k3dkiqiwqokow'))

html = """
<div><p>如果你为门中弟子伤她一分，我便屠你满门</p></div>
<div><p>如果你为天下人损她一毫，我便杀尽天下人</p></div>
"""

pattern = re.compile(r'<div><p>(.*?)</p></div>', re.S)
print(pattern.findall(html))
