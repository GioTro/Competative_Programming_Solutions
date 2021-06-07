# Solution for kattis problem source:
# https://open.kattis.com/problems/securedoors

integer = input()
entries = []
names = []
for i in range(0, integer):
    Strings = (str, raw_input())
    entries.append(Strings[1])

for i in range(0, len(entries)):
    if entries[i].split(' ', 1)[0] == "entry":
        if entries[i].split(' ', 1)[1] not in names:
            name = entries[i].split(' ', 1)[1]
            names.append(name)
            print("%s entered" % (name))
        else:
            name = entries[i].split(' ', 1)[1]
            print("%s entered (ANOMALY)" % (name))
    if entries[i].split(' ', 1)[0] == "exit":
        name = entries[i].split(' ', 1)[1]
        if name in names:
            names.remove(name)
            print("%s exited" % (name))
        else:
            print("%s exited (ANOMALY)" % (name))
