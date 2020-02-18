f = open("talk.txt")
list_people = []
for line in f:
    name = line.split(":", 1)[0]
    if name not in list_people:
        file = open(name + ".txt","w")
        file.write(line)
        list_people.append(name)
    else:
        file = open(name + ".txt", "a")
        file.write(line)
