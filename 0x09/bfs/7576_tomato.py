# https://www.acmicpc.net/problem/7576
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def solution(M, N, board, queue):
    date = 0
    while queue:
        x, y, d = queue.popleft()
        date = d
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            ni = ny * M + nx
            if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ni]:
                continue
            board[ni] = -1
            queue.append((nx, ny, d + 1))

    return date if sum(board) == - N * M else -1


IM, IN = map(int, sys.stdin.readline().split())
IBoard, IQueue = [], deque()
for iy in range(IN):
    for ix, t in enumerate(map(int, sys.stdin.readline().split())):
        if t == 1:
            IBoard.append(-1)
            IQueue.append((ix, iy, 0))
        else:
            IBoard.append(t)
print(solution(IM, IN, IBoard, IQueue))


