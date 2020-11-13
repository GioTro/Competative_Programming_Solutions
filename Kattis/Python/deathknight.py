#Solotion for kattis problem source: https://open.kattis.com/problems/deathknight

limit = int(input())
count = 0
for i in range(0, limit):
    battle = input()
    if len(battle)>1:
        if 'CD' in battle:
            count += 1
print(limit-count)
