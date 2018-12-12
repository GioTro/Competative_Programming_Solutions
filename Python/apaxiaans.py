#Solution for kattis problem source: https://open.kattis.com/problems/apaxiaaans

def stringmagician(string):
    letter = string[0]
    name = letter
    for i in range(1, len(string)):
        if letter != string[i]:
            letter = string[i]
            name += letter
    return str(name)

#HandleInput
print(stringmagician(str(raw_input())))
