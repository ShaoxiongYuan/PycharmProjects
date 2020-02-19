import re

s = """
Hello
北京
"""

# regex=re.compile(r"[a-z]+",flags=re.IGNORECASE)
# regex = re.compile(r"^北京", flags=re.MULTILINE)
# regex = re.compile(r".+", flags=re.DOTALL)
regex = re.compile(r"\w+", flags=re.ASCII)

print(regex.findall(s))
