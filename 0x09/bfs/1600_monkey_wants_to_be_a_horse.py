# https://www.acmicpc.net/problem/1600
import sys
from collections import deque


m_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
h_dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def solutions(K, M, N, board):
    if M == 1 and N == 1:
        return 0

    visited = [[[False] * IM for _ in range(IN)] for _ in range(IK + 1)]
    queue = deque([(0, 0, K)])
    dist = 0
    while queue:
        dist += 1
        for _ in range(len(queue)):
            x, y, k = queue.popleft()
            for (dx, dy) in m_dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= M or ny < 0 or ny >= N or \
                        visited[k][ny][nx] or board[ny][nx] == '1':
                    continue
                if (nx, ny) == (M - 1, N - 1):
                    return dist
                visited[k][ny][nx] = True
                queue.append((nx, ny, k))

            if k > 0:
                for (dx, dy) in h_dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= M or ny < 0 or ny >= N or \
                            visited[k - 1][ny][nx] or board[ny][nx] == '1':
                        continue
                    if (nx, ny) == (M - 1, N - 1):
                        return dist
                    visited[k - 1][ny][nx] = True
                    queue.append((nx, ny, k - 1))
    return -1


IK = int(sys.stdin.readline())
IM, IN = map(int, sys.stdin.readline().split())
IBoard = [list(sys.stdin.readline().split()) for _ in range(IN)]
print(solutions(IK, IM, IN, IBoard))
