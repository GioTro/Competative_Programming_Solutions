# problem: https://open.kattis.com/problems/anewalphabet

language = {
    "a": "@",
    "b": "8",
    "c": "(",
    'd': "|)",
    "e": "3",
    "f": "#",
    "g": "6",
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "[]\\/[]",
    "n": "[]\\[]",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "r": "|Z",
    "s": "$",
    "t": "']['",
    "u": "|_|",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "}{",
    "y": "`/",
    "z": "2"
}


def solve(n):
    res = ""
    for i in range(len(n)):
        if n[i].lower() in language.keys():
            res += language[n[i].lower()]
        else:
            res += n[i]
    return res


print(solve(str(raw_input())))
