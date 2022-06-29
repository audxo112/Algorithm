# https://www.acmicpc.net/problem/13460
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def move(board, x, y, ox, oy, dx, dy):
    crash = False
    while board[y + dy][x + dx] != "#":
        x, y = x + dx, y + dy
        if board[y][x] == "O":
            return x, y, True, crash
        if (x, y) == (ox, oy):
            crash = True
    if crash:
        x, y = x - dx, y - dy
    return x, y, False, crash


def bfs(board, visited, rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by)])
    visited.add((rx, ry, bx, by))
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            orx, ory, obx, oby = queue.popleft()
            for dr in range(4):
                dx, dy = dirs[dr]
                bx, by, bo, bc = move(board, obx, oby, orx, ory, dx, dy)
                if bo:
                    continue
                if bc:
                    rx, ry = bx + dx, by + dy
                else:
                    rx, ry, ro, _ = move(board, orx, ory, obx, oby, dx, dy)
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
    for (x, y) in [(x, y) for y in range(1, N - 1) for x in range(1, M - 1)]:
        if board[y][x] == "R":
            rx, ry = x, y
            if bx:
                break
        elif board[y][x] == "B":
            bx, by = x, y
            if rx:
                break
    return bfs(board, visited, rx, ry, bx, by)


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().rstrip() for _ in range(IN)]
print(solution(IN, IM, IBoard))
