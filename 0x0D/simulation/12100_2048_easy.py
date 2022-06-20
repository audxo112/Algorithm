# https://www.acmicpc.net/problem/12100
import sys


def merge_horizontal(N, board, sn, en, step):
    nboard = [[0] * N for _ in range(N)]
    for y in range(N):
        i, before = sn, 0
        for x in range(sn, en, step):
            if board[y][x]:
                if before:
                    if before == board[y][x]:
                        nboard[y][i] = before + board[y][x]
                        before = 0
                    else:
                        nboard[y][i] = before
                        before = board[y][x]
                    i += step
                else:
                    before = board[y][x]
        if before:
            nboard[y][i] = before
    return nboard


def merge_vertical(N, board, sn, en, step):
    nboard = merge_horizontal(N, list(zip(*board)), sn, en, step)
    return list(zip(*nboard))


def dfs(N, M, board):
    if M == 0:
        return max([max(b) for b in board])

    val = 0
    val = max(dfs(N, M - 1, merge_horizontal(N, board, 0, N, 1)), val)
    val = max(dfs(N, M - 1, merge_horizontal(N, board, N - 1, -1, -1)), val)
    val = max(dfs(N, M - 1, merge_vertical(N, board, 0, N, 1)), val)
    val = max(dfs(N, M - 1, merge_vertical(N, board, N - 1, -1, -1)), val)
    return val


def solution(N, board):
    return dfs(N, 5, board)


IN = int(sys.stdin.readline())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IBoard))
