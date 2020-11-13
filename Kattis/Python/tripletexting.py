# Solution tripletexting
line = input().strip()
break_point = int(len(line) / 3)

print(line[:break_point] if line[:break_point] in line[break_point:] else line[break_point:-break_point])

