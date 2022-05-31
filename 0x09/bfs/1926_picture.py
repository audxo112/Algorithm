# https://www.acmicpc.net/problem/1926
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def bfs(N, M, board, sx, sy):
    board[sy][sx] = '0'
    queue = deque([(sx, sy)])
    area = 1
    while queue:
        x, y = queue.popleft()

        for (dx, dy) in dirs:
            nx, ny = dx + x, dy + y
            if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ny][nx] == '0':
                continue
            else:
                board[ny][nx] = '0'
                area += 1
                queue.append((nx, ny))
    return area


def solution(N, M, board):
    cnt = maxVal = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == '1':
                cnt += 1
                maxVal = max(bfs(N, M, board, x, y), maxVal)
    print(cnt)
    print(maxVal)


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(sys.stdin.readline().split()) for _ in range(IN)]
solution(IN, IM, IBoard)

