# https://www.acmicpc.net/problem/2178
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


def solution(N, M, board):
    queue = deque([(0, 0)])
    board[0][0] = '0'
    dist = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for nx, ny in move(N, M, x, y):
                if board[ny][nx] == '0':
                    continue
                if (nx, ny) == (M - 1, N - 1):
                    return dist + 1

                board[ny][nx] = '0'
                queue.append((nx, ny))
        dist += 1


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(sys.stdin.readline().rstrip()) for _ in range(IN)]
print(solution(IN, IM, IBoard))

