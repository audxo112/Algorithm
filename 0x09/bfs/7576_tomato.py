# https://www.acmicpc.net/problem/7576
import sys
from collections import deque


def move(N, M, x, y):
    if x + 1 < M:
        yield x + 1, y
    if x - 1 >= 0:
        yield x - 1, y
    if y + 1 < N:
        yield x, y + 1
    if y - 1 >= 0:
        yield x, y - 1


def bfs(M, N, board, queue):
    date = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for nx, ny in move(N, M, x, y):
                if board[ny][nx]:
                    continue
                board[ny][nx] = -1
                queue.append((nx, ny))
        date += 1
    return date - 1 if sum(sum(board, [])) == - N * M else -1


def solution(M, N, board):
    queue = deque()
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                board[y][x] = -1
                queue.append((x, y))

    return bfs(M, N, board, queue)


IM, IN = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
print(solution(IM, IN, IBoard))
