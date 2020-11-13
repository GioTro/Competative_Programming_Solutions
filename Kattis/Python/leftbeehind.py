# problem : https://open.kattis.com/problems/leftbeehind

def solve(p, q):
    if p+q == 13:
        return 'Never speak again.'
    if p == q:
        return 'Undecided.'
    if p > q:
        return 'To the convention.'
    if p < q:
        return 'Left beehind.'
        



p, q = 1, 1

while True:
    p, q = map(int, input().split())
    if [p, q] == [0, 0]:
        break
    else:
        print(solve(p, q))
