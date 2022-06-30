# https://www.acmicpc.net/problem/15685
import sys


dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def simulation(board, curve):
    x, y, sdr, cnt = curve
    board[y][x] = 1

    stack = []
    for _ in range(cnt + 1):
        n = len(stack)
        if stack:
            for i in range(n - 1, -1, -1):
                dr = stack[i]
                stack.append((dr + 1) % 4)
        else:
            stack.append(sdr)

        for i in range(n, len(stack)):
            dr = stack[i]
            dx, dy = dirs[dr]
            x, y = x + dx, y + dy
            board[y][x] = 1


def solution(N, curves):
    board = [[0] * 101 for _ in range(101)]

    for curve in curves:
        simulation(board, curve)

    cnt = 0
    for y in range(100):
        for x in range(100):
            if board[y][x] and board[y + 1][x] and board[y][x + 1] and board[y + 1][x + 1]:
                cnt += 1
    return cnt


IN = int(sys.stdin.readline())
ICurves = [tuple(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, ICurves))
