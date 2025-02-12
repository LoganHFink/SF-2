F,D = input('Input Franchises, Days: ').split()

grid = []

for k in range(int(D)):
    grid.append(input(f"Day {k + 1}: ").split())

dozens = 0

# Horizontal

for row in grid:
    total = 0
    for sale in row:
        total += int(sale)
    if total % 13 == 0:
        dozens += total/13
        print("got a horizontal dozen")

# Vertical

for column in range(len(grid)-1):
    total = 0
    for i in range(int(D)):
        total += int(grid[i][column])
    if total % 13 == 0:
        dozens += total/13
        print("got a vertical dozen")

print(int(dozens))