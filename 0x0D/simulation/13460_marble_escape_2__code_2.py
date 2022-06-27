# https://www.acmicpc.net/problem/13460
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def move(N, M, board, x, y, ox, oy, dr):
    dx, dy = dirs[dr]
    crash = False
    while 1 <= x < M - 1 and 1 <= y < N - 1 and board[y + dy][x + dx] != "#":
        x, y = x + dx, y + dy
        if board[y][x] == "O":
            return x, y, True
        if (x, y) == (ox, oy):
            crash = True
    if crash:
        x, y = x - dx, y - dy
    return x, y, False


def bfs(N, M, board, visited, rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by)])
    visited.add((rx, ry, bx, by))
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            orx, ory, obx, oby = queue.popleft()
            for dr in range(4):
                bx, by, bo = move(N, M, board, obx, oby, orx, ory, dr)
                if bo:
                    continue
                rx, ry, ro = move(N, M, board, orx, ory, obx, oby, dr)
                if ro:
                    return cnt

                if (rx, ry, bx, by) in visited:
                    continue
                visited.add((rx, ry, bx, by))
                queue.append((rx, ry, bx, by))
        if cnt == 10:
            break
    return -1


def solution(N, M, board):
    visited = set()
    rx = ry = bx = by = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == "R":
                rx, ry = x, y
                if bx:
                    break
            elif board[y][x] == "B":
                bx, by = x, y
                if rx:
                    break
    return bfs(N, M, board, visited, rx, ry, bx, by)


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().rstrip() for _ in range(IN)]
print(solution(IN, IM, IBoard))
