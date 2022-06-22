# https://www.acmicpc.net/problem/14499
import sys


def rolling(dice, bottom, dr):
    if dr == 3 or dr == 4:
        dice = list(map(list, zip(*dice)))
    if dr == 1 or dr == 3:
        dice[1], bottom = [bottom] + dice[1][:-1], dice[1][-1]
    else:
        dice[1], bottom = dice[1][1:] + [bottom], dice[1][0]
    if dr == 3 or dr == 4:
        dice = list(map(list, zip(*dice)))
    return dice, bottom


def solution(N, M, x, y, K, board, drs):
    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    dice = [['0'] * 3 for y in range(3)]
    bottom = "0"
    answer = []

    for dr in drs:
        dx, dy = dirs[dr - 1]
        if 0 <= x + dx < M and 0 <= y + dy < N:
            x, y = x + dx, y + dy
            dice, bottom = rolling(dice, bottom, dr)
            if board[y][x] != "0":
                bottom, board[y][x] = board[y][x], "0"
            else:
                board[y][x] = bottom
            answer.append(dice[1][1])
    return "\n".join(answer)


IN, IM, ISY, ISX, IK = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
IDrs = list(map(int, sys.stdin.readline().split()))
print(solution(IN, IM, ISX, ISY, IK, IBoard, IDrs))
