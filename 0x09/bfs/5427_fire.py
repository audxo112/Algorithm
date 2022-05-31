# https://www.acmicpc.net/problem/5427
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def init_board(W, H, board, queue):
    fire, flag = [], True
    for y in range(IH):
        for x, c in enumerate(sys.stdin.readline().strip()):
            if c == "*":
                fire.append((x, y, 1, "F"))
                board.append("#")
            elif c == "@":
                if x == 0 or x == W - 1 or y == 0 or y == H - 1:
                    flag = False
                queue.append((x, y, 1, "P"))
                board.append(".")
            else:
                board.append(c)
    queue.extendleft(fire)
    return flag


def solution(W, H, board, queue):
    while queue:
        x, y, dist, tp = queue.popleft()

        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= W or ny < 0 or ny >= H or board[ny * W + nx] == "#" or (tp == "P" and board[ny * W + nx] == "%"):
                continue
            if tp == "F":
                board[ny * W + nx] = "#"
                queue.append((nx, ny, dist + 1, "F"))
            elif tp == "P":
                if nx == 0 or nx == W - 1 or ny == 0 or ny == H - 1:
                    return dist + 1

                board[ny * W + nx] = "%"
                queue.append((nx, ny, dist + 1, "P"))
    return "IMPOSSIBLE"


IT = int(sys.stdin.readline().strip())
for _ in range(IT):
    IW, IH = map(int, sys.stdin.readline().split())
    IBoard, IQueue = [], deque()
    if init_board(IW, IH, IBoard, IQueue):
        print(solution(IW, IH, IBoard, IQueue))
    else:
        print(1)

