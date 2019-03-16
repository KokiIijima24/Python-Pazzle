# 数独の再帰的解法
backtracks = 0

input = [
[5,1,7,6,0,0,0,3,4],
[2,8,9,0,0,4,0,0,0],
[3,4,6,2,0,5,0,9,0],
[6,0,2,0,0,0,0,1,0],
[0,3,8,0,0,6,0,4,7],
[0,0,0,0,0,0,0,0,0],
[0,9,0,0,0,0,0,7,8],
[7,0,3,4,0,0,5,6,0],
[0,0,0,0,0,0,0,0,0]
]


def solveSudoku(grid, i = 0, j = 0):
    global backtracks
    i, j = findNextCellTo(grid)
    if (i == -1):
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if (solveSudoku(grid, i, j)):
                return True
            backtracks += 1
    grid[i][j] = 0
    return False

def findNextCellTo(grid):
    # 左上から右下へ向かって探索
    for x in range(9):
        for y in range(9):
            if (grid[x][y] == 0):
                return x, y
    return -1, -1

def isValid(grid, i, j, e):
    row0k = all([e != grid[i][x] for x in range(9)])
    if row0k:
        column0k = all(e != grid[x][j] for x in range(9))
        if column0k:
            SecTopX, SecTopY = 3 * (i // 3), 3 * (j // 3)
            for x in range(SecTopX, SecTopX + 3):
                for y in range(SecTopY, SecTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False

def PrintSudoku(grid):
    narrow = 0
    for row in grid:
        if narrow % 3 == 0 and narrow != 0:
            print(' ')
        print(row[0:3], ' ', row[3:6], ' ', row[6:9])
        narrow += 1

solveSudoku(input)
PrintSudoku(input)

print(backtracks)
