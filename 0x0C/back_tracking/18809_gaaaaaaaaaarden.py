# https://www.acmicpc.net/problem/18809
import sys
from collections import deque


def back_tracking(candi, M, n = 0, visited=[]):
    N = len(candi)
    if N - n < M:
        return

    if M == 0:
        return [list(map(lambda x: candi[x], visited))]

    pos = []
    for i in range(n, N):
        visited.append(i)
        if result := back_tracking(candi, M - 1, i + 1, visited):
            pos.extend(result)
        visited.pop()
    return pos


def dirs(N, M, x, y):
    if x + 1 < M:
        yield x + 1, y
    if x - 1 >= 0:
        yield x - 1, y
    if y + 1 < N:
        yield x, y + 1
    if y - 1 >= 0:
        yield x, y - 1


def bfs(N, M, board, green, red):
    visited = [[0] * M for _ in range(N)]
    g_queue, r_queue = deque(green), deque(red)
    for x, y in green:
        visited[y][x] = -1
    for x, y in red:
        visited[y][x] = -1

    flower, time = 0, 1
    while g_queue and r_queue:
        for _ in range(len(g_queue)):
            x, y = g_queue.popleft()
            if visited[y][x] == -2:
                continue

            for nx, ny in dirs(N, M, x, y):
                if board[ny][nx] == "0" or visited[ny][nx]:
                    continue
                visited[ny][nx] = time
                g_queue.append((nx, ny))

        for _ in range(len(r_queue)):
            x, y = r_queue.popleft()

            for nx, ny in dirs(N, M, x, y):
                if board[ny][nx] == "0" or visited[ny][nx] < 0:
                    continue

                if visited[ny][nx] == time:
                    visited[ny][nx] = -2
                    flower += 1
                elif not visited[ny][nx]:
                    visited[ny][nx] = -1
                    r_queue.append((nx, ny))
        time += 1
    return flower


def solution(N, M, G, R, board):
    candi = [(x, y) for x in range(M) for y in range(N) if board[y][x] == "2"]
    flower = 0
    for pos in back_tracking(candi, G + R):
        for green in back_tracking(pos, G):
            red = [x for x in pos if x not in green]
            flower = max(bfs(N, M, board, green, red), flower)

    return flower


IN, IM, IG, IR = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
print(solution(IN, IM, IG, IR, IBoard))
