# https://www.acmicpc.net/problem/2448
import sys


def split(N, sx, sy):
    yield sx, sy
    yield sx - N // 2, sy + N // 2
    yield sx + N // 2, sy + N // 2


def plist(sx, sy):
    yield sx, sy
    yield sx - 1, sy + 1
    yield sx - 2, sy + 2
    yield sx - 1, sy + 2
    yield sx, sy + 2
    yield sx + 1, sy + 2
    yield sx + 2, sy + 2
    yield sx + 1, sy + 1


def recursion(N, board, sx, sy):
    if N == 3:
        for x, y in plist(sx, sy):
            board[y][x] = "*"
        return

    nn = N // 2
    for x, y in split(N, sx, sy):
        recursion(nn, board, x, y)


def solution(N):
    board = [[" "] * (2 * N - 1) for _ in range(N)]
    recursion(N, board, N - 1, 0)
    return board


IN = int(sys.stdin.readline())
OAnswer = solution(IN)
for OAns in OAnswer:
    print("".join(OAns))
