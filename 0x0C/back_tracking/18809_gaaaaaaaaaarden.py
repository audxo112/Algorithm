# https://www.acmicpc.net/problem/18809
import sys
from collections import deque


isG, isR = {"G": 1, "R": 0, "X": 0}, {"G": 0, "R": 1, "X": 0}


def back_tracking(N, G, R, candi, n, visited, cases):
    if N == n:
        if G + R == 0:
            cases.append([(*candi[i], c, 1) for i, c in enumerate(visited) if c != "X"])
        return

    for xgr in "XGR":
        g, r = G - isG[xgr], R - isR[xgr]
        if g < 0 or r < 0 or N - n - 1 < g + r:
            continue
        visited.append(xgr)
        back_tracking(N, g, r, candi, n + 1, visited, cases)
        visited.pop()


def dirs(N, M, x, y):
    if x + 1 < M:
        yield x + 1, y
    if x - 1 >= 0:
        yield x - 1, y
    if y + 1 < N:
        yield x, y + 1
    if y - 1 >= 0:
        yield x, y - 1


def bfs(N, M, board, case):
    visited = [[0] * M for _ in range(N)]
    dist = [[0] * M for _ in range(N)]
    for x, y, tp, d in case:
        visited[y][x] = tp
        dist[y][x] = d

    queue = deque(case)
    flower = 0
    while queue:
        x, y, tp, d = queue.popleft()
        if visited[y][x] == "F":
            continue

        for nx, ny in dirs(N, M, x, y):
            if board[ny][nx] == "0" or visited[ny][nx] == "F":
                continue

            if visited[ny][nx]:
                if visited[ny][nx] != tp and dist[ny][nx] == d + 1:
                    visited[ny][nx] = "F"
                    flower += 1
            else:
                visited[ny][nx] = tp
                dist[ny][nx] = d + 1
                queue.append((nx, ny, tp, d + 1))

    return flower


def solution(N, M, G, R, board):
    pos = [(x, y) for x in range(M) for y in range(N)]
    candi = [(x, y) for (x, y) in pos if board[y][x] == "2"]

    cases = []
    back_tracking(len(candi), G, R, candi, 0, [], cases)
    flower = 0
    for case in cases:
        flower = max(bfs(N, M, board, case), flower)
    return flower


IN, IM, IG, IR = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
print(solution(IN, IM, IG, IR, IBoard))
