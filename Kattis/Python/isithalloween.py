facit = {
    "OCT": 31,
    "DEC": 25
}

d = list(map(str, raw_input().split()))
if d[0] in facit.keys():
    if facit[d[0]] == int(d[1]):
        print('yup')
    else:
        print('nope')
else:
    print('nope')
