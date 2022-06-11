# https://www.acmicpc.net/problem/2630
import sys


def split(N, sx, sy):
    yield sx, sy
    yield sx + N, sy
    yield sx, sy + N
    yield sx + N, sy + N


def recursion(N, board, sx, sy):
    if N == 1:
        return (0, 1) if board[sy][sx] else (1, 0)

    nn = N // 2
    z = o = 0
    for (x, y) in split(nn, sx, sy):
        cz, co = recursion(nn, board, x, y)
        z += cz
        o += co

    if z == 0:
        return 0, 1
    elif o == 0:
        return 1, 0
    else:
        return z, o


def solution(N, board):
    return recursion(N, board, 0, 0)


IN = int(sys.stdin.readline())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
OAnswer = solution(IN, IBoard)
for OAns in OAnswer:
    print(OAns)
