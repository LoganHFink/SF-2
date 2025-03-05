# Sliding puzzle part 2
# Logan Fink
# Student code: 2435373

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

def makeMove(board,move):
    y,x = findEmptyTile(board)
    if move == 'W':
        board[y][x],board[y-1][x] = board[y-1][x],board[y][x]
    if move == 'A':
        board[y][x],board[y][x-1] = board[y][x-1],board[y][x]
    if move == 'S':
        board[y][x],board[y+1][x] = board[y+1][x],board[y][x]
    if move == 'D':
        board[y][x],board[y][x+1] = board[y][x+1],board[y][x]

def checkGameState(board,moves_left):
    y,x = findEmptyTile(board)
    board_1d = []
    for yi in range(len(board)):
        for xi in range(len(board)):
            if xi != x or yi != y:
                board_1d.append(int(board[yi][xi][0:2]))
    moves_left[0] -= 1
    if board_1d == sorted(board_1d) and moves_left[0] >= 0:
        return 'win'
    elif moves_left[0] <= 0:
        return 'lose'
    
    if moves_left[0] < 81:
        print(f'{moves_left[0]} move(s) remaining')

# Main Program start:

print('Welcome to sliding block puzzle')
print('Use the WASD keys to move the empty tile around until all tiles are in increasing order')
print('For a 9 tile board you have 31 moves to win, for a 16 tile one, you have 80')
n = int(input('Enter the length/width of the board (integer): '))

board = getNewPuzzle(int(n))

displayBoard(board)

if n == 3:
    moves_left = [31]
elif n == 4:
    moves_left = [80]
else:
    moves_left = [9999999999]

over = False
while not over:
    move = nextMove(board)
    if move != None:
        makeMove(board,move)
        displayBoard(board)
        game_state = checkGameState(board,moves_left) 
        if game_state == 'win':
            print("YOU WIN, HERE'S A CONGRATULATORY MESSAGE!!!")
            over = True
        if game_state == 'lose':
            print('Best of luck next time!')
            over = True
