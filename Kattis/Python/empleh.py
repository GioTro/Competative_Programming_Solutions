# Problem : https://open.kattis.com/problems/empleh
import re


def makePlaceholderBoard():
    b = '|.*.|:*:|.*.|:*:|.*.|:*:|.*.|:*:|'
    c = '|:*:|.*.|:*:|.*.|:*:|.*.|:*:|.*.|'
    board, t = [], True
    for i in range(8):
        if t:
            board.append(b)
            t = not t
        else:
            board.append(c)
            t = not t
    return board


def p(l):
    board = makePlaceholderBoard()
    row = 8
    index = 0
    for i in board:
        column = 'a'
        for j in range(len(i)):
            if i[j] != '*':
                continue
            else:
                t = column + str(row)
                if t in l.keys():
                    board[index] = board[index][:j] + \
                        l[t] + board[index][j + 1:]
                else:
                    board[index] = board[index][:j] + \
                        i[j - 1] + board[index][j + 1:]
            column = chr(ord(column) + 1)
        row -= 1
        index += 1

    a = '+---+---+---+---+---+---+---+---+'
    print(a)
    for i in board:
        print(i)
        print(a)


white = re.findall('[A-Z]?[a-h][1-8](?=,)', str(input()) + ',')
black = re.findall('[A-Z]?[a-h][1-8](?=,)', str(input()) + ',')
board = {}

for i in white:
    if len(i) == 2:
        board.update({i: 'P'})
    else:
        board.update({i[1:]: i[0]})

for i in black:
    if len(i) == 2:
        board.update({i: 'p'})
    else:
        board.update({i[1:]: i[0].lower()})

p(board)
