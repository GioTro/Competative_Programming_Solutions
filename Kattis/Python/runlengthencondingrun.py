# Solution : https://open.kattis.com/problems/runlengthencodingrun

def encode(s):
    res = s[0]
    count = 0
    for i in range(1, len(s)):
        if res[-1] != s[i]:
            if count == 0:
                res += "1" + s[i]
            else:
                res += str(count + 1) + s[i]
                count = 0
        else:
            count += 1
    return res + str(count + 1)


def decode(s):
    res = ""
    i = 0
    while (i < len(s)):
        res += s[i]
        for j in range(int(s[i + 1]) - 1):
            res += s[i]
        i += 2
    return res


d, s = map(str, raw_input().split())

if d == 'E':
    print(encode(s))
else:
    print(decode(s))

#print(encode("HHHeellloWooorrrrlld!!") == "H3e2l3o1W1o3r4l2d1!2")
#print(decode("H3e2l3o1W1o3r4l2d1!2") == "HHHeellloWooorrrrlld!!")
