# https://www.acmicpc.net/problem/2178
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def solution(N, M, board):
    queue = deque([(0, 0, 1)])
    board[0][0] = '0'
    while queue:
        x, y, dist = queue.popleft()

        for (dx, dy) in dirs:
            nx, ny = dx + x, dy + y
            if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ny][nx] == '0':
                continue
            if (nx, ny) == (M - 1, N - 1):
                return dist + 1

            board[ny][nx] = '0'
            queue.append((nx, ny, dist + 1))


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(sys.stdin.readline().strip()) for _ in range(IN)]
print(solution(IN, IM, IBoard))

