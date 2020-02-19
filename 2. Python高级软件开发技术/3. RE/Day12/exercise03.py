import re

print(re.search(r"(\d{1,3}\.){3}\d{1,3}", "IPv4:192.168.0.114").group())
print(re.findall(r"《.+?》", "《红与黑》   《百年孤独》"))
print(re.findall(r"\d{4}-\d{1,2}-\d{1,2}", "1984-10-24     1990-5-6     1993-05-03"))
print(re.findall(r"\d{18}[A-Z]*", "身份证号：500106200203123819"))
