import sys
from collections import deque


def directions(y, x, row, col):
    if x + 1 < col:
        yield x + 1, y
    if x - 1 >= 0:
        yield x - 1, y
    if y + 1 < row:
        yield x, y + 1
    if y - 1 >= 0:
        yield x, y - 1


def solution(board, ROW, COL, K):
    if ROW == 1 and COL == 1:
        return 1

    dist = [[[-1] * COL for _ in range(ROW)] for _ in range(K + 1)]
    dist[0][0][0] = 1
    queue = deque([[0, 0, 0]])

    while queue:
        broken, y, x = queue.popleft()

        for nx, ny in directions(y, x, ROW, COL):
            if ny == ROW - 1 and nx == COL - 1:
                return dist[broken][y][x] + 1
            if board[ny][nx] == 0 and dist[broken][ny][nx] == -1:
                dist[broken][ny][nx] = dist[broken][y][x] + 1
                queue.append([broken, ny, nx])

            if broken < K and board[ny][nx] == 1 and dist[broken + 1][ny][nx] == -1:
                dist[broken + 1][ny][nx] = dist[broken][y][x] + 1
                queue.append([broken + 1, ny, nx])

    return -1


ROW, COL, IT = map(int, sys.stdin.readline().split())
BOARD = [list(map(int, sys.stdin.readline().strip())) for _ in range(ROW)]

print(solution(BOARD, ROW, COL, IT))