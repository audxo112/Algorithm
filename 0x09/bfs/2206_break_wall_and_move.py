# https://www.acmicpc.net/problem/2206
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(N, M, board):
    if N == 1 and M == 1:
        return 1

    visited = [[2] * M for _ in range(N)]
    visited[0][0] = 0
    queue = deque([(0, 0)])
    dist = 1
    while queue:
        dist += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for (dx, dy) in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                k = board[ny][nx] + visited[y][x]
                if k < visited[ny][nx] and k <= 1:
                    if (nx, ny) == (M - 1, N - 1):
                        return dist
                    visited[ny][nx] = k
                    queue.append((nx, ny))
    return -1


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(IN)]
print(solution(IN, IM, IBoard))

