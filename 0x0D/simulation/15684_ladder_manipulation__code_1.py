# https://www.acmicpc.net/problem/15684
import sys


R, L = 1, 2


def simulation(N, H, board):
    for n in range(N):
        c = n
        for h in range(H):
            if board[h][c] == R:
                c += 1
            elif board[h][c] == L:
                c -= 1
        if c != n:
            return False
    return True


def back_tracking(C, N, H, board, pos):
    if C == 3:
        return -1

    if simulation(N, H, board):
        return C

    for x, y in pos:
        if board[y][x] or board[y][x + 1]:
            continue
        board[y][x], board[y][x + 1] = R, L
        if simulation(N, H, board):
            return C + 1
        board[y][x], board[y][x + 1] = 0, 0

    for x, y in pos:
        if board[y][x] or board[y][x + 1]:
            continue
        board[y][x], board[y][x + 1] = R, L
        result = back_tracking(C + 1, N, H, board, pos)
        if result != -1:
            return result
        board[y][x], board[y][x + 1] = 0, 0
    return -1


def solution(N, M, H, line):
    board = [[0] * (N) for _ in range(H)]
    for y, x in line:
        board[y - 1][x] = L
        board[y - 1][x - 1] = R
    pos = [(x, y) for y in range(H) for x in range(N - 1) if board[y][x] == 0 and board[y][x + 1] == 0]

    return back_tracking(0, N, H, board, pos)


IN, IM, IH = map(int, sys.stdin.readline().split())
ILine = [tuple(map(int, sys.stdin.readline().split())) for _ in range(IM)]
print(solution(IN, IM, IH, ILine))
