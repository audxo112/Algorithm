# https://www.acmicpc.net/problem/17144
import sys


dirs = [
    [(1, 0), (0, -1), (-1, 0), (0, 1)],
    [(1, 0), (0, 1), (-1, 0), (0, -1)],
]
RU, RD = 0, 1


def simulation_dust(R, C, board, vacuum):
    nxt = [[0] * C for _ in range(R)]
    nxt[vacuum][0] = nxt[vacuum + 1][0] = -1
    for y in range(R):
        for x in range(C):
            if board[y][x] > 0:
                div = board[y][x] // 5
                cnt = 0
                for dx, dy in dirs[0]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= C or ny < 0 or ny >= R or board[ny][nx] == -1:
                        continue
                    cnt += 1
                    nxt[ny][nx] += div
                nxt[y][x] += board[y][x] - div * cnt
    return nxt


def simulation_vacuum(R, C, board, x, y, ro):
    dr = tmp = 0
    while dr < 4:
        dx, dy = dirs[ro][dr]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= C or ny < 0 or ny >= R or board[ny][nx] == -1:
            dr += 1
            continue
        board[ny][nx], tmp = tmp, board[ny][nx]
        x, y = nx, ny


def solution(R, C, T, board):
    vacuum = 0
    for y in range(R):
        if board[y][0] == -1:
            vacuum = y
            break

    for _ in range(T):
        board = simulation_dust(R, C, board, vacuum)
        simulation_vacuum(R, C, board, 0, vacuum, 0)
        simulation_vacuum(R, C, board, 0, vacuum + 1, 1)

    return sum(sum(board, [])) + 2


IR, IC, IT = map(int, sys.stdin.readline().split())
IBoard = [list(map(int,sys.stdin.readline().split())) for _ in range(IR)]
print(solution(IR, IC, IT, IBoard))
