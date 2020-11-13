# Problem : https://open.kattis.com/problems/permutationencryption
import re
def chop(s, n):
    # Add padding
    while len(s)%n != 0:
        s += ' '

    regex = '.{'+str(n)+'}'
    return re.findall(regex, s)

def solve(string, keys, le):
    ret = ''
    while len(string) > 0:
        j = 0
        placeholder = ['x' for _ in range(len(string[0]))]
        for i in string[0]:
            placeholder[keys[j]] = i
            j += 1
        string = string[1:]
        ret += "".join(placeholder)
    return ret
            
    
while True:
    p = list(map(int, input().split()))
    if p[0] == 0 and len(p) == 1:
        break
    else:
        p = p[1:]
        s = str(input())
        t = len(s)
        string = chop(s, len(p))

        # Construct a dictionairy
        mapping, j = {}, 0
        for i in p:
            mapping.update({i-1:j})
            j += 1
        print("'"+solve(string, mapping, t)+"'")
