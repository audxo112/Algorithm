# https://www.acmicpc.net/problem/7569
import sys
from collections import deque


dirs = [(0, 1, 0), (-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1)]


def bfs(M, N, H, board, queue):
    cur = -1
    while queue:
        x, y, z, cnt = queue.popleft()
        cur = cnt
        board[z * M * N + y * M + x] = -1

        for (dx, dy, dz) in dirs:
            nx, ny, nz = x + dx, y + dy, z + dz
            if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H or board[nz * M * N + ny * M + nx]:
                continue
            board[nz * M * N + ny * M + nx] = -1
            queue.append((nx, ny, nz, cnt + 1))
    return cur


def solution(M, N, H, board, queue):
    result = bfs(M, N, H, board, queue)
    if sum(board) == - M * N * H:
        return result
    else:
        return -1


IM, IN, IH = map(int, sys.stdin.readline().split())
IBoard = []
IQueue = deque()
for z in range(IH):
    for y in range(IN):
        for x, t in enumerate(map(int, sys.stdin.readline().split())):
            if t == 1:
                IQueue.append((x, y, z, 0))
            IBoard.append(t)

print(solution(IM, IN, IH, IBoard, IQueue))

