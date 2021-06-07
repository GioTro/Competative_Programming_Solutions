# Problem : https://open.kattis.com/problems/mia
def solve(p_1, p_2):
    score = [0, 0]

    if p_1 == '21' or p_1 == '12':
        score[0] = str(200)
    elif p_1[0] == p_1[1]:
        score[0] = str(1) + p_1
    else:
        if int(p_1[0]) > int(p_1[1]):
            score[0] = p_1
        else:
            score[0] = p_1[::-1]

    if p_2 == '21' or p_2 == '12':
        score[1] = str(200)
    elif p_2[0] == p_2[1]:
        score[1] = str(1) + p_2
    else:
        if int(p_2[0]) > int(p_2[1]):
            score[1] = p_2
        else:
            score[1] = p_2[::-1]

    if int(score[0]) > int(score[1]):
        return 'Player 1 wins.'
    elif int(score[0]) < int(score[1]):
        return 'Player 2 wins.'
    else:
        return 'Tie.'


while True:
    s_0, s_1, r_0, r_1 = map(str, raw_input().split())
    if [s_0, s_1, r_0, r_1] == ['0', '0', '0', '0']:
        break
    else:
        print(solve(s_0 + s_1, r_0 + r_1))
