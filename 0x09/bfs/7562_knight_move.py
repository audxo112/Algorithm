# https://www.acmicpc.net/problem/7562
import sys
from collections import deque


dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def solution(N, cx, cy, tx, ty):
    if (cx, cy) == (tx, ty):
        return 0

    visited = [[False] * N for _ in range(N)]
    visited[cy][cx] = True

    queue = deque([(cx, cy, 0)])
    while queue:
        x, y, step = queue.popleft()

        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[ny][nx]:
                continue
            if (nx, ny) == (tx, ty):
                return step + 1
            visited[ny][nx] = True
            queue.append((nx, ny, step + 1))
    return 0


IT = int(sys.stdin.readline().strip())
for _ in range(IT):
    IN = int(sys.stdin.readline().strip())
    ICX, ICY = map(int, sys.stdin.readline().split())
    ITX, ITY = map(int, sys.stdin.readline().split())
    print(solution(IN, ICX, ICY, ITX, ITY))

