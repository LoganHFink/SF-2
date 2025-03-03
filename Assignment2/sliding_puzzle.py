import random
import sys

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def tileLabels(n):
    output = [str(x) for x in range(1,n*n)]
    output.append('  ')
    return output

def getNewPuzzle(n):
    tiles = tileLabels(n)
    new_tiles = []
    for t in tiles:
        if len(t) == 1:
            t += ' '
        new_tiles.append(t)
    random.shuffle(new_tiles)

    board = []

    slice_start = 0
    for _ in range(n):    
        board.append(new_tiles[slice_start:slice_start+n])
        slice_start += n 
    return board

def findEmptyTile(board):
    n = len(board)
    for row in range(n):
        for column in range(n):
            if board[row][column] == '  ':
                return (row,column)

def nextMove(board):
    n = len(board)
    valid_moves = ['W','A','S','D']
    emptyy,emptyx = findEmptyTile(board)
    if emptyx == n-1:
        valid_moves[3] = ' '
    if emptyx == 0:
        valid_moves[1] = ' '
    if emptyy == n-1:
        valid_moves[2] = ' '
    if emptyy == 0:
        valid_moves[0] = ' '

    print(f'                          ({valid_moves[0]})')
    print(f'Enter WASD (or QUIT): ({valid_moves[1]}) ({valid_moves[2]}) ({valid_moves[3]})')
    move = input('> ').upper()
    if move == 'QUIT':
        sys.exit()
    if move in valid_moves:
        return move

# Program start:

board = getNewPuzzle(4)
displayBoard(board)

over = False
while not over:
    nextMove(board)
