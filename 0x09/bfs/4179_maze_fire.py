# https://www.acmicpc.net/problem/4179
import sys
from collections import deque


INF = 1000000
N, M = map(int, sys.stdin.readline().split())
board = [[INF] * M for _ in range(N)]
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
fire = []
queue = deque()
for i in range(N):
    for j, c in enumerate(sys.stdin.readline().strip()):
        if c == "#":
            board[i][j] = -1
        elif c == "F":
            board[i][j] = 0
            fire.append((j, i))
        elif c == "J":
            queue.append((j, i, 1))


def oor(x, y):
    return x < 0 or x >= M or y < 0 or y >= N


def bfs():
    global fire
    b_step = 0
    while queue:
        x, y, step = queue.popleft()
        if x == 0 or x == M - 1 or y == 0 or y == N - 1:
            return step

        if b_step < step:
            b_step = step
            nf = []
            for (fx, fy) in fire:
                for (dx, dy) in dirs:
                    nx, ny = fx + dx, fy + dy
                    if oor(nx, ny) or board[ny][nx] <= board[fy][fx] + 1:
                        continue
                    board[ny][nx] = board[fy][fx] + 1
                    nf.append((nx, ny))
            fire = nf

        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if oor(nx, ny) or board[ny][nx] <= step + 1:
                continue

            if nx == 0 or nx == M - 1 or ny == 0 or ny == N - 1:
                return step + 1
            board[ny][nx] = step + 1
            queue.append((nx, ny, step + 1))

    return "IMPOSSIBLE"


print(bfs())

