# https://www.acmicpc.net/problem/1012
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def bfs(M, N, board, sx, sy):
    queue = deque([(sx, sy)])

    while queue:
        x, y = queue.popleft()

        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N or not board[ny][nx]:
                continue
            board[ny][nx] = 0
            queue.append((nx, ny))

    return 1


def solution(M, N, pos):
    board = [[0] * M for _ in range(N)]
    for (px, py) in pos:
        board[py][px] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x]:
                cnt += bfs(M, N, board, x, y)
    return cnt


IT = int(sys.stdin.readline().strip())
for _ in range(IT):
    IM, IN, IK = map(int, sys.stdin.readline().split())
    IPos = [list(map(int, sys.stdin.readline().split())) for _ in range(IK)]
    print(solution(IM, IN, IPos))

