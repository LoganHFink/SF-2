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
    output += ' '
    return output
            
# print(tileLabels(3))

def getNewPuzzle(n):
    tiles = tileLabels(n)
    tiles = [t + ' ' for t in tiles if len(t) == 1 and t != ' ']
    tiles.append('  ')
    random.shuffle(tiles)

    output = []

    slice_start = 0
    slice_end = n
    for _ in range(n):    
        output.append(tiles[slice_start:slice_end])
        slice_start += n 
        slice_end += n
    return output

# print(getNewPuzzle(3))

def findEmptyTile(board):
    n = len(board)
    for y in range(n):
        for x in range(n):
            if board[y][x] == '  ':
                return (x,y)

# board = getNewPuzzle(3)
# displayBoard(board)
# print(findEmptyTile(board))

def nextMove(board):
    n = len(board)
    valid_moves = ['W','A','S','D']
    emptyx,emptyy = findEmptyTile(board)
    # print(emptyx,emptyy)
    if emptyx == n-1:
        # print('right')
        valid_moves[3] = ' '
    if emptyx == 0:
        # print('left')
        valid_moves[1] = ' '
    if emptyy == n-1:
        # print('bottom')
        valid_moves[2] = ' '
    if emptyy == 0:
        # print('top')
        valid_moves[0] = ' '

    print(f'                          ({valid_moves[0]})')
    print(f'Enter WASD (or QUIT): ({valid_moves[1]}) ({valid_moves[2]}) ({valid_moves[3]})')
    move = input('>')
    if move.upper() == 'QUIT':
        sys.exit()
    if move.upper() in valid_moves:
        print(move)


board = getNewPuzzle(3)
displayBoard(board)
while True:
    nextMove(board)
