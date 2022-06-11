# https://www.acmicpc.net/problem/1780
import sys


dic = {
    -1: (1, 0, 0),
    0: (0, 1, 0),
    1: (0, 0, 1),
}


def split(N, sx, sy):
    yield sx, sy
    yield sx, sy + N
    yield sx, sy + 2 * N
    yield sx + N, sy
    yield sx + N, sy + N
    yield sx + N, sy + 2 * N
    yield sx + 2 * N, sy
    yield sx + 2 * N, sy + N
    yield sx + 2 * N, sy + 2 * N


def recursion(N, board, sx, sy):
    if N == 1:
        return dic[board[sy][sx]]

    nn = N // 3
    a = b = c = 0
    for (x, y) in split(nn, sx, sy):
        ca, cb, cc = recursion(nn, board, x, y)
        a, b, c = a + ca, b + cb, c + cc

    if a == 0 and b == 0:
        return 0, 0, 1
    elif a == 0 and c == 0:
        return 0, 1, 0
    elif b == 0 and c == 0:
        return 1, 0, 0
    else:
        return a, b, c


def solution(N, board):
    return recursion(N, board, 0, 0)


IN = int(sys.stdin.readline())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
OAnswer = solution(IN, IBoard)
for OAns in OAnswer:
    print(OAns)
