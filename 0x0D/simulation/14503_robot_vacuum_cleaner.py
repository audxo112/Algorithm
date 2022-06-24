# https://www.acmicpc.net/problem/14503
import sys


dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def simulation(x, y, d, board, clean):
    if board[y][x] == "0":
        board[y][x] = '2'
        clean += 1

    for _ in range(4):
        d = (d + 3) % 4
        dx, dy = dirs[d]
        nx, ny = x + dx, y + dy
        if board[ny][nx] == "0":
            return simulation(nx, ny, d, board, clean)
    else:
        dx, dy = dirs[(d + 2) % 4]
        bx, by = x + dx, y + dy
        if board[by][bx] == "1":
            return clean
        return simulation(bx, by, d, board, clean)


def solution(N, M, R, C, D, board):
    return simulation(C, R, D, board, 0)


IN, IM = map(int, sys.stdin.readline().split())
IR, IC, ID = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
print(solution(IN, IM, IR, IC, ID, IBoard))
