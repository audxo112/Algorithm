# https://www.acmicpc.net/problem/4991
import sys
from collections import deque, defaultdict
from itertools import permutations


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# def bfs(W, H, board, dist, pos):
#     PN = len(pos)
#     visited = [[[False] * W for _ in range(H)] for _ in range(PN)]
#     for i, x, y in pos:
#         visited[i][y][x] = True
#     cnt = [1] * PN
#
#     queue = deque(pos)
#     d = 1
#     while queue:
#         for _ in range(len(queue)):
#             i, x, y = queue.popleft()
#             for dx, dy in dirs:
#                 nx, ny = x + dx, y + dy
#                 if nx < 0 or nx >= W or ny < 0 or ny >= H or board[ny][nx] == "x" or visited[i][ny][nx]:
#                     continue
#
#                 for pi in range(PN):
#                     if i == pi or dist[i][pi] != 9999:
#                         continue
#                     if visited[pi][ny][nx]:
#                         if pi > i:
#                             dist[i][pi] = dist[pi][i] = d * 2 - 1
#                         else:
#                             dist[i][pi] = dist[pi][i] = d * 2
#                         cnt[i] += 1
#                         cnt[pi] += 1
#                 if cnt[i] < PN:
#                     visited[i][ny][nx] = True
#                     queue.append((i, nx, ny))
#         d += 1
#
#
# def solution(W, H, board):
#     pos = deque()
#     for y in range(H):
#         for x in range(W):
#             if board[y][x] == "o":
#                 pos.appendleft((x, y))
#             elif board[y][x] == "*":
#                 pos.append((x, y))
#
#     pos = [(i, x, y) for i, (x, y) in enumerate(pos)]
#     print(pos)
#
#     PN = len(pos)
#     dist = [[9999] * PN for _ in range(PN)]
#     bfs(W, H, board, dist, pos)
#     for d in dist:
#         print(d)
#     print()
#
#     return sum([dist[i][j] for i in range(PN) for j in range(i + 1, PN) if dist[i][j] != 9999])

def bfs(W, H, board, graph, PN, sx, sy):
    visited = [[False] * W for _ in range(H)]
    visited[sy][sx] = True

    queue = deque([(sx, sy)])
    time = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= W or ny < 0 or ny >= H or visited[ny][nx] or board[ny][nx] == "x":
                    continue
                visited[ny][nx] = True
                queue.append((nx, ny))
                if board[ny][nx] == "*" or board[ny][nx] == "o":
                    if (nx, ny) in graph[(sx, sy)]:
                        continue
                    graph[(sx, sy)][(nx, ny)] = time
                    graph[(nx, ny)][(sx, sy)] = time
                    if len(graph[(sx, sy)]) == PN:
                        return graph
        time += 1


def solution(W, H, board):
    pos = deque()
    for y in range(H):
        for x in range(W):
            if board[y][x] == "o":
                pos.appendleft((x, y))
            elif board[y][x] == "*":
                pos.append((x, y))
    PN = len(pos) - 1
    graph = defaultdict(dict)
    for x, y in pos:
        if len(graph[(x, y)]) == PN:
            continue
        bfs(W, H, board, graph, PN, x, y)
        if len(graph[(x, y)]) < PN:
            return -1

    print(graph)
    best = 4000
    visited = set()
    # for p in pos:
    dist = 0
    cur = pos.popleft()
    for _ in range(PN - 1):
        mp = None
        md = 4000
        for p, d in graph[cur].items():
            if p in visited:
                continue
            if md > d:
                md = d



    # print(graph)
    # for route in permutations(pos, PN):
    #     dist = graph[vacuum][route[0]]
    #     for i in range(PN - 1):
    #         dist += graph[route[i]][route[i + 1]]
    #     if dist < best:
    #         best = dist
    return best



import time

total = 0
while True:
    IW, IH = map(int, sys.stdin.readline().split())
    if not IW or not IH:
        break
    IBoard = [sys.stdin.readline().rstrip() for _ in range(IH)]
    start = time.time()
    print(solution(IW, IH, IBoard))
    total += time.time() - start
print(total)
