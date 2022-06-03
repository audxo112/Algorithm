# https://www.acmicpc.net/problem/11967
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(N, graph):
    light = [[0] * N for _ in range(N)]
    light[0][0] = 1
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 2
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for lx, ly in graph[y][x]:
            light[ly][lx] = 1
            if visited[ly][lx] == 1:
                queue.append((lx, ly))
        else:
            graph[y][x].clear()

        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[ny][nx]:
                continue
            if light[ny][nx]:
                visited[ny][nx] = 2
                queue.append((nx, ny))
            else:
                visited[ny][nx] = 1

    return sum(map(sum, light))


IN, IM = map(int, sys.stdin.readline().split())
IGraph = [[[] for _ in range(IN)] for _ in range(IN)]
for _ in range(IM):
    IX, IY, IA, IB = map(int, sys.stdin.readline().split())
    IGraph[IY - 1][IX - 1] += [(IA - 1, IB - 1)]
print(solution(IN, IGraph))
