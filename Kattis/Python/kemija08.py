# Problem : https://open.kattis.com/problems/kemija08

vowels = ['a', 'e', 'i', 'o', 'u']

string = str(raw_input())
res = ""
i = 0
while i < len(string):
    res += string[i]
    if string[i] in vowels:
        i += 3
    else:
        i += 1

print res
