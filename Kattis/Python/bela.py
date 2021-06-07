# Solution for Kattis problem source: https://open.kattis.com/problems/bela

def scoreboard(card, dominant):
    string = "AKQJT987"
    score = [[11, 4, 3, 20, 10, 14, 0, 0], [11, 4, 3, 2, 10, 0, 0, 0]]
    index = 0
    for i in range(0, len(string)):
        if card == string[i]:
            index = i
            break
    if dominant:
        return score[0][index]
    else:
        return score[1][index]


limit, dominant = (input().split())
limit = 4 * int(limit)
summa = 0
cards = []

for i in range(0, limit):
    cards.append(str(input()))

for i in range(0, len(cards)):
    if cards[i][1] == dominant:
        summa += scoreboard(cards[i][0], True)
    else:
        summa += scoreboard(cards[i][0], False)

print(summa)
