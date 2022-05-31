# https://www.acmicpc.net/problem/2667
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def bfs(N, board, sx, sy):
    queue = deque([(sx, sy)])
    board[sy][sx] = '0'
    area = 1
    while queue:
        x, y = queue.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx] == '0':
                continue
            board[ny][nx] = '0'
            area += 1
            queue.append((nx, ny))
    return area


def solution(N, board):
    answer = []
    for y in range(N):
        for x in range(N):
            if board[y][x] == '1':
                answer.append(bfs(N, board, x, y))
    return sorted(answer)


IN = int(sys.stdin.readline())
IBoard = [list(sys.stdin.readline()) for _ in range(IN)]
OAnswer = solution(IN, IBoard)
print(len(OAnswer))
for OA in OAnswer:
    print(OA)

