# https://www.acmicpc.net/problem/2146
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(N, board, gid, sx, sy):
    queue = deque([(sx, sy)])
    board[sy][sx] = gid
    candi = set()
    while queue:
        x, y = queue.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx] > 1:
                continue
            if board[ny][nx] == 0:
                candi.add((x, y))
                continue
            board[ny][nx] = gid
            queue.append((nx, ny))
    return candi


def solution(N, board):
    queue, gid, loop = deque(), 1, 1

    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                gid += 1
                queue.extend(bfs(N, board, gid, x, y))

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for (dx, dy) in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if board[ny][nx] == 0:
                    board[ny][nx] = board[y][x]
                    queue.append((nx, ny))
                elif board[ny][nx] > board[y][x]:
                    return (loop - 1) * 2
                elif board[ny][nx] < board[y][x]:
                    return loop * 2 - 1
        loop += 1

    return N * N


IN = int(sys.stdin.readline())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IBoard))
