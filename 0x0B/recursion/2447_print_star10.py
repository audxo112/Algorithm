# https://www.acmicpc.net/problem/2447
import sys


def split(N, sx, sy):
    yield sx, sy
    yield sx + N, sy
    yield sx + 2 * N, sy
    yield sx, sy + N
    yield sx + 2 * N, sy + N
    yield sx, sy + 2 * N
    yield sx + N, sy + 2 * N
    yield sx + 2 * N, sy + 2 * N


def recursion(N, board, sx, sy):
    if N == 3:
        board[sy + 1][sx + 1] = " "
        return

    nn = N // 3
    for x, y in split(nn, sx, sy):
        recursion(nn, board, x, y)

    for y in range(sy + nn, sy + 2 * nn):
        for x in range(sx + nn, sx + 2 * nn):
            board[y][x] = " "


def solution(N):
    board = [["*"] * N for _ in range(N)]
    recursion(N, board, 0, 0)
    return board


IN = int(sys.stdin.readline())
OAnswer = solution(IN)
for OAns in OAnswer:
    print("".join(OAns))

