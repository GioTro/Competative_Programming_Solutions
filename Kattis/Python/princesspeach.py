# Problem : https://open.kattis.com/problems/princesspeach
p, q = map(int, input().split())
d = [int(input()) for _ in range(q)]
for i in range(p):
    if i not in d:
        print(i)
print("Mario got {} of the dangerous obstacles.".format(len(set(d))))
