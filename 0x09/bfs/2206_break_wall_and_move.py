# https://www.acmicpc.net/problem/2206
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def solution(N, M, board, visited):
    queue = deque([(0, 0, 1, True)])
    while queue:
        x, y, dist, chance = queue.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            ni = ny * M + nx
            if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[ni] or (not chance and board[ni] == '1'):
                continue
            if nx == M - 1 and ny == N - 1:
                return dist + 1
            visited[ni] = True
            if board[ni] == '1' and chance:
                queue.append((nx, ny, dist + 1, False))
            elif board[ni] == '0':
                queue.append((nx, ny, dist + 1, chance))
    return -1


IN, IM = map(int, sys.stdin.readline().split())
IVisited = [True] + [False] * (IN * IM - 1)
IBoard = []
for _ in range(IN):
    IBoard.extend(list(sys.stdin.readline().strip()))
print(solution(IN, IM, IBoard, IVisited))

