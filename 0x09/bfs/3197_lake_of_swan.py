# https://www.acmicpc.net/problem/3197
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(R, C, board, swan, oid, sx, sy):
    ice = set()
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()

        if board[y][x] == "L":
            swan.append(oid)
            board[y][x] = oid
        elif board[y][x] == ".":
            board[y][x] = oid

        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= C or ny < 0 or ny >= R or type(board[ny][nx]) is int:
                continue
            if board[ny][nx] == "X":
                ice.add((x, y))
            else:
                queue.append((nx, ny))
    return ice


def meet(swans, a, b):
    if a > b:
        a, b = b, a
    if swans[0] == b:
        swans[0] = a
    if swans[1] == b:
        swans[1] = a
    return swans[0] == swans[1]


def solution(R, C, board):
    queue, swans = [], []
    oid = 0
    for y in range(R):
        for x in range(C):
            if board[y][x] == "." or board[y][x] == "L":
                queue.extend(bfs(R, C, board, swans, oid, x, y))
                oid += 1
    date = 0
    while queue:
        date += 1
        tmp = []
        for x, y in queue:
            for (dx, dy) in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= C or ny < 0 or ny >= R:
                    continue
                if board[ny][nx] == "X":
                    board[ny][nx] = board[y][x]
                    tmp.append((nx, ny))
                elif board[y][x] < board[ny][nx]:
                    if meet(swans, board[y][x], board[ny][nx]):
                        return date - 1
                    board[ny][nx] = board[y][x]
                elif board[y][x] > board[ny][nx]:
                    if meet(swans, board[ny][nx], board[y][x]):
                        return date
                    board[y][x] = board[ny][nx]
        queue = tmp


IR, IC = map(int, sys.stdin.readline().split())
IBoard = [list(sys.stdin.readline().rstrip()) for _ in range(IR)]
print(solution(IR, IC, IBoard))

