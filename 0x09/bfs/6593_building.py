# https://www.acmicpc.net/problem/6593
import sys
from collections import deque


dirs = [(0, 1, 0), (-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1)]


def init_board(L, R, C, board, visited, queue):
    for z in range(L):
        for y in range(R):
            for x, b in enumerate(sys.stdin.readline().strip()):
                if b == "S":
                    visited[z * R * C + y * C + x] = True
                    queue.append((x, y, z))
                    board.append(".")
                else:
                    board.append(b)
        else:
            sys.stdin.readline()


def solution(L, R, C, board, visited, queue):
    dist = 0
    while queue:
        dist += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()

            for (dx, dy, dz) in dirs:
                nx, ny, nz = x + dx, y + dy, z + dz
                ni = nz * R * C + ny * C + nx
                if nx < 0 or nx >= C or ny < 0 or ny >= R or nz < 0 or nz >= L or visited[ni] or board[ni] == "#":
                    continue
                if board[ni] == "E":
                    return f"Escaped in {dist} minute(s)."
                visited[ni] = True
                queue.append((nx, ny, nz))
    return "Trapped!"


while True:
    IL, IR, IC = map(int, sys.stdin.readline().split())
    if IL == 0 or IR == 0 or IC == 0:
        break
    IBoard, IQueue = [], deque()
    IVisited = [False] * (IL * IR * IC)
    init_board(IL, IR, IC, IBoard, IVisited, IQueue)
    print(solution(IL, IR, IC, IBoard, IVisited, IQueue))

