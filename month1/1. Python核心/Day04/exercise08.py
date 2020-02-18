planet = ["金星", "地球", "火星", "木星", "土星", "天王星", ]
planet.insert(0, "水星")
planet.append("海王星")
print(planet[:2:])
for i in range(2, 8):
    print(planet[i])

for i in range(len(planet) - 1, -1, -1):
    print(planet[i])