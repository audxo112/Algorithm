# https://www.acmicpc.net/problem/16234
import sys


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

    group = dict()
    population = dict()
    date = 0
    while True:
        cid = 0
        for y in range(N):
            for x in range(N):
                if visited[y][x] < date:
                    g, p = bfs(N, L, R, board, visited, x, y, date)
                    if len(g) > 1:
                        group[cid] = g
                        population[cid] = p
                        cid += 1
        if cid == 0:
            return date
        for i in range(cid):
            for x, y in group[i]:
                board[y][x] = population[i] // len(group[i])
            group[i].clear()
        date += 1


IN, IL, IR = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IL, IR, IBoard))
