#!python3
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    linetop = board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']
    linemid = board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']
    linelow = board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']
    print(linetop.center(5))
    print('-+-+-')
    print(linemid.center(5))
    print('-+-+-')
    print(linelow.center(5))


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on witch space? ')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
