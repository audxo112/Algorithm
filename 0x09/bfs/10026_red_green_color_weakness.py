# https://www.acmicpc.net/problem/10026
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def bfs(N, board, visited, sx, sy, found):
    queue = deque([(sx, sy)])
    visited[sy][sx] = True

    while queue:
        x, y = queue.popleft()

        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[ny][nx] or board[ny][nx] not in found:
                continue
            visited[ny][nx] = True
            queue.append((nx, ny))

    return 1


def solution(N, board):
    n_visited = [[False] * N for _ in range(N)]
    rgw_visited = [[False] * N for _ in range(N)]
    rgw = {"R": "RG", "G": "RG", "B": "B"}

    n_cnt = rgw_cnt = 0
    for y in range(N):
        for x in range(N):
            if not n_visited[y][x]:
                n_cnt += bfs(N, board, n_visited, x, y, board[y][x])
            if not rgw_visited[y][x]:
                rgw_cnt += bfs(N, board, rgw_visited, x, y, rgw[board[y][x]])

    return " ".join(map(str, [n_cnt, rgw_cnt]))


IN = int(sys.stdin.readline().strip())
IBoard = [list(sys.stdin.readline().strip()) for _ in range(IN)]

print(solution(IN, IBoard))

