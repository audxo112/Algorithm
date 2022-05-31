# https://www.acmicpc.net/problem/2583
import sys
from collections import deque


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def init_board(M, N, K, board):
    for _ in range(K):
        sx, sy, tx, ty = map(int, sys.stdin.readline().split())
        board[sy][sx] = board[sy][sx] + 1
        if tx < M:
            board[sy][tx] = board[sy][tx] - 1
        if ty < N:
            board[ty][sx] = board[ty][sx] - 1
        if tx < M and ty < N:
            board[ty][tx] = board[ty][tx] + 1

    for y in range(N):
        for x in range(1, M):
            board[y][x] = board[y][x] + board[y][x - 1]
    for x in range(M):
        for y in range(1, N):
            board[y][x] = board[y][x] + board[y - 1][x]


def bfs(M, N, board, sx, sy):
    queue = deque([(sx, sy)])
    board[sy][sx] = 1
    area = 1
    while queue:
        x, y = queue.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ny][nx]:
                continue
            board[ny][nx] = 1
            area += 1
            queue.append((nx, ny))
    return area


def solutions(M, N, board):
    answer = []
    for y in range(N):
        for x in range(M):
            if not board[y][x]:
                answer.append(bfs(M, N, board, x, y))

    return sorted(answer)


IN, IM, IK = map(int, sys.stdin.readline().split())
IBoard = [[0] * IM for _ in range(IN)]
init_board(IM, IN, IK, IBoard)
OAnswer = solutions(IM, IN, IBoard)
print(len(OAnswer))
print(" ".join(map(str, OAnswer)))

