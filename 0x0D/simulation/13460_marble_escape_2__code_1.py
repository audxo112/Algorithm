# https://www.acmicpc.net/problem/13460
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
diffs = {"B": "R", "R": "B"}


def move(board, color, x, y, ox, oy, dr, outs):
    dx, dy = dirs[dr]
    mvs = []
    while True:
        if board[y][x] == ".":
            x, y = x + dx, y + dy
            if (x, y) == (ox, oy):
                mvs = move(board, diffs[color], ox, oy, x, y, dr, outs)
                if mvs:
                    diff, dfx, dfy = mvs[0]
                    return mvs + [(color, dfx - dx, dfy - dy)]
                else:
                    return mvs
        elif board[y][x] == "#":
            return mvs + [(color, x - dx, y - dy)]
        else:
            outs.append(color)
            return mvs


def bfs(board, rx, ry, bx, by):
    queue = deque([
        (rx, ry, bx, by, 0),
        (rx, ry, bx, by, 1),
        (rx, ry, bx, by, 2),
        (rx, ry, bx, by, 3)
    ])
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            orx, ory, obx, oby, dr = queue.popleft()
            rx, ry, bx, by = orx, ory, obx, oby
            outs = []
            mvs = move(board, "R", orx, ory, obx, oby, dr, outs)
            for color, mvx, mvy in mvs:
                if color == "R":
                    rx, ry = mvx, mvy
                else:
                    bx, by = mvx, mvy

            if len(mvs) == 2 and (orx, ory, obx, oby) != (rx, ry, bx, by):
                queue.extend([(rx, ry, bx, by, (dr + i) % 4) for i in range(1, 4)])
                continue
            if outs and "B" in outs:
                continue

            mvs = move(board, "B", bx, by, rx, ry, dr, outs)
            for color, mvx, mvy in mvs:
                if color == "R":
                    rx, ry = mvx, mvy
                else:
                    bx, by = mvx, mvy
            if outs:
                if len(outs) == 1 and outs[0] == "R":
                    return cnt
                continue

            if (orx, ory, obx, oby) != (rx, ry, bx, by):
                queue.extend([(rx, ry, bx, by, (dr + i) % 4) for i in range(1, 4)])
        if cnt == 10:
            break
    return -1


def solution(N, M, board):
    marbles = dict()
    for (x, y) in [(x, y) for x in range(M) for y in range(N)]:
        if board[y][x] == "R" or board[y][x] == "B":
            marbles[board[y][x]] = (x, y)
            board[y] = board[y].replace(board[y][x], ".")
            if len(marbles) == 2:
                break
    return bfs(board, *marbles["R"], *marbles["B"])


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().rstrip() for _ in range(IN)]
print(solution(IN, IM, IBoard))
