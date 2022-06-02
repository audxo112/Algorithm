# https://www.acmicpc.net/problem/16933
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(N, M, K, board):
    if N == 1 and M == 1:
        return 1

    broken = [[K + 1] * M for _ in range(N)]
    broken[0][0] = 0
    queue = deque([(0, 0, 0)])
    time = 1
    while queue:
        time += 1
        for _ in range(len(queue)):
            x, y, k = queue.popleft()
            for (dx, dy) in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= M or ny < 0 or ny >= N or k >= broken[ny][nx]:
                    continue
                if board[ny][nx] == '0':
                    if (nx, ny) == (M - 1, N - 1):
                        return time
                    broken[ny][nx] = k
                    queue.append((nx, ny, k))
                else:
                    if k + 1 >= broken[ny][nx]:
                        continue
                    elif time % 2 == 0:
                        broken[ny][nx] = k + 1
                        queue.append((nx, ny, k + 1))
                    else:
                        queue.append((x, y, k))
    return -1


IN, IM, IK = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().rstrip() for _ in range(IN)]
print(solution(IN, IM, IK, IBoard))
