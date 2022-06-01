# https://www.acmicpc.net/problem/4179
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def init_board(R, C, board, queue):
    fire = []
    for y in range(R):
        for x, c in enumerate(sys.stdin.readline().strip()):
            if c == "F":
                fire.append((x, y, 1, "F"))
                board.append("#")
            elif c == "J":
                if x == 0 or x == C - 1 or y == 0 or y == R - 1:
                    return False
                queue.append((x, y, 1, "P"))
                board.append(".")
            else:
                board.append(c)
    queue.extendleft(fire)
    return True


def solution(R, C, board, queue):
    while queue:
        x, y, dist, tp = queue.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            ni = ny * C + nx
            if nx < 0 or nx >= C or ny < 0 or ny >= R or board[ni] == "#" or (tp == "P" and board[ni] == "%"):
                continue
            if tp == "F":
                board[ni] = "#"
                queue.append((nx, ny, dist + 1, "F"))
            elif tp == "P":
                if nx == 0 or nx == C - 1 or ny == 0 or ny == R - 1:
                    return dist + 1

                board[ni] = "%"
                queue.append((nx, ny, dist + 1, "P"))
    return "IMPOSSIBLE"


IR, IC = map(int, sys.stdin.readline().split())
IBoard, IQueue = [], deque()
if init_board(IR, IC, IBoard, IQueue):
    print(solution(IR, IC, IBoard, IQueue))
else:
    print(1)