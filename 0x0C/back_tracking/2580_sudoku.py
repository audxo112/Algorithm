# https://www.acmicpc.net/problem/2580
import sys


def back_tracking(pos, board, row, col, block, i):
    if len(pos) == i:
        return True
    x, y = pos[i]
    bi = (y // 3) * 3 + x // 3
    for num in range(1, 10):
        if row[y][num] or col[x][num] or block[bi][num]:
            continue
        row[y][num] = col[x][num] = block[bi][num] = True
        board[y][x] = num
        if back_tracking(pos, board, row, col, block, i + 1):
            return True
        row[y][num] = col[x][num] = block[bi][num] = False
        board[y][x] = 0
    return False


def solution(board):
    pos = [(x, y) for y in range(9) for x in range(9) if not board[y][x]]
    row = [[False] * 10 for _ in range(9)]
    col = [[False] * 10 for _ in range(9)]
    block = [[False] * 10 for _ in range(9)]
    for y in range(9):
        for x in range(9):
            bi, num = (y // 3) * 3 + x // 3, board[y][x]
            row[y][num] = col[x][num] = block[bi][num] = True
    back_tracking(pos, board, row, col, block, 0)

    return "\n".join([" ".join(map(str, b)) for b in board])


IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
print(solution(IBoard))
