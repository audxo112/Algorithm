# https://www.acmicpc.net/problem/2468
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def bfs(N, board, visited, sx, sy, water):
    queue = deque([(sx, sy)])
    visited[sy * N + sx] = water
    while queue:
        x, y = queue.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[ny * N + nx] == water or board[ny * N + nx] < water:
                continue
            visited[ny * N + nx] = water
            queue.append((nx, ny))
    return 1


def solution(N, board):
    minH, maxH = min(board) + 1, max(board)
    if minH == maxH + 1:
        return 1
    visited = [0] * (N * N)
    answer = 0

    for h in range(minH, maxH + 1):
        cnt = 0
        for y in range(N):
            for x in range(N):
                if visited[y * N + x] < h <= board[y * N + x]:
                    cnt += bfs(N, board, visited, x, y, h)
        answer = max(cnt, answer)
    return answer


IN = int(sys.stdin.readline())
IBoard = []
for _ in range(IN):
    IBoard.extend(list(map(int, sys.stdin.readline().split())))

print(solution(IN, IBoard))

