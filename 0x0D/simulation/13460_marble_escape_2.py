# https://www.acmicpc.net/problem/13460
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
diffs = {"B": "R", "R": "B"}


def move(board, color, x, y, ox, oy, dr):
    dx, dy = dirs[dr]
    mvs, outs = [], []
    while True:
        if board[y][x] == ".":
            x, y = x + dx, y + dy
            if (x, y) == (ox, oy):
                mvs, outs = move(board, diffs[color], ox, oy, x, y, dr)
                if mvs:
                    diff, dfx, dfy = mvs[0]
                    return mvs + [(color, dfx - dx, dfy - dy)], outs
                else:
                    return mvs, outs + [color]
        elif board[y][x] == "#":
            return mvs + [(color, x - dx, y - dy)], outs
        else:
            return mvs, outs + [color]


def bfs(board, rx, ry, bx, by):
    queue = deque([
        (rx, ry, bx, by, 0),
        (rx, ry, bx, by, 1),
        (rx, ry, bx, by, 2),
        (rx, ry, bx, by, 3)
    ])
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            orx, ory, obx, oby, odr = queue.popleft()
            rx, ry, bx, by = orx, ory, obx, oby
            mvs, outs = move(board, "R", orx, ory, obx, oby, odr)
            if mvs:
                for color, mvx, mvy in mvs:
                    if color == "R":
                        rx, ry = mvx, mvy
                    elif
                if len(mvs) == 2:
                    queue.extend([(rx, ry, bx, by, (dr + i) % 4) for i in range(1, 3)])
                    break
            else:
                if len(outs) == 1 and outs[0] == "R":
                    return cnt
                break
            mvs, outs = move(board, "B", rx, ry, bx, by, dr)
        cnt += 1
        if cnt == 6:
            break
    return -1


def solution(N, M, board):
    marbles = dict()
    for (x, y) in [(x, y) for x in range(M) for y in range(N)]:
        if board[y][x] == "R" or board[y][x] == "B":
            marbles[board[y][x]] = (x, y)
            board[y].replace(board[y][x], ".")
            if len(marbles) == 2:
                break
    return bfs(board, *marbles["R"], *marbles["B"])


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().rstrip() for _ in range(IN)]
print(solution(IN, IM, IBoard))
