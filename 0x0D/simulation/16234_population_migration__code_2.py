# https://www.acmicpc.net/problem/16234
import sys
from collections import deque


def move(N, x, y):
    if x > 0:
        yield x - 1, y
    if x + 1 < N:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y + 1 < N:
        yield x, y + 1


def bfs(N, L, R, board, visited, sx, sy, date):
    visited[sy][sx] = date
    queue = [(sx, sy)]
    population = board[sy][sx]
    for x, y in queue:
        for nx, ny in move(N, x, y):
            diff = abs(board[ny][nx] - board[y][x])
            if diff < L or diff > R or visited[ny][nx] == date:
                continue
            visited[ny][nx] = date
            population += board[ny][nx]
            queue.append((nx, ny))
    return queue, population


def solution(N, L, R, board):
    visited = [[-1] * N for _ in range(N)]
    pos = deque([(x, y) for y in range(N) for x in range(y % 2, N, 2)])

    date = 0
    while pos:
        for _ in range(len(pos)):
            x, y = pos.popleft()
            if visited[y][x] < date:
                g, p = bfs(N, L, R, board, visited, x, y, date)
                if len(g) > 1:
                    avg = p // len(g)
                    for x, y in g:
                        board[y][x] = avg
                        pos.append((x, y))
        if pos:
            date += 1
    return date


IN, IL, IR = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IL, IR, IBoard))
