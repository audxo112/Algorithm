# https://www.acmicpc.net/problem/2573
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(N, M, board, visited, melt, sx, sy):
    queue = deque([(sx, sy)])
    visited.add((sx, sy))

    while queue:
        x, y = queue.popleft()
        melt[(x, y)] = 0
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N or (nx, ny) in visited:
                continue
            if board[ny][nx] <= 0:
                melt[(x, y)] += 1
                continue
            visited.add((nx, ny))
            queue.append((nx, ny))
    return 1


def solution(N, M, board, ice):
    visited, melt, year = set(), dict(), 0
    while ice:
        cnt = 0
        for (ix, iy) in ice:
            if (ix, iy) not in visited:
                if cnt + 1 > 1:
                    return year
                cnt += bfs(N, M, board, visited, melt, ix, iy)

        for (mx, my) in melt.keys():
            board[my][mx] -= melt[(mx, my)]
            if board[my][mx] <= 0:
                ice.remove((mx, my))

        year += 1
        melt.clear()
        visited.clear()
    return 0


IN, IM = map(int, sys.stdin.readline().split())
IBoard = []
IIce = set()
for IY in range(IN):
    line = list(map(int, sys.stdin.readline().split()))
    for IX, IC in enumerate(line):
        if IC > 0:
            IIce.add((IX, IY))
    IBoard.append(line)
print(solution(IN, IM, IBoard, IIce))
