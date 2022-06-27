# https://www.acmicpc.net/problem/14502
import sys
from itertools import combinations


def move(N, M, x, y):
    if x - 1 >= 0:
        yield x - 1, y
    if x + 1 < M:
        yield x + 1, y
    if y - 1 >= 0:
        yield x, y - 1
    if y + 1 < N:
        yield x, y + 1


def bfs(N, M, board, plague, visited, zero):
    queue = [] + plague
    for x, y in queue:
        for nx, ny in move(N, M, x, y):
            if board[ny][nx] != "0" or visited[ny][nx]:
                continue
            zero -= 1
            visited[ny][nx] = True
            queue.append((nx, ny))
    return zero


def solution(N, M, board):
    plague = [(x, y) for x in range(M) for y in range(N) if board[y][x] == "2"]
    visited = [[False] * M for _ in range(N)]
    for px, py in plague:
        visited[py][px] = True
    pos = [(x, y) for x in range(M) for y in range(N) if board[y][x] == "0"]
    maxi, zero = 0, len(pos) - 3

    for blank in combinations(pos, 3):
        for bx, by in blank:
            board[by][bx] = "1"
        maxi = max(bfs(N, M, board, plague, [v[:] for v in visited], zero), maxi)
        for bx, by in blank:
            board[by][bx] = "0"

    return maxi


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
print(solution(IN, IM, IBoard))
