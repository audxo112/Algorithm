# https://www.acmicpc.net/problem/3197
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(R, C, board, visited, oid, sx, sy, swans):
    visited[sy][sx] = True
    ice = set()
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()

        if board[y][x] == ".":
            board[y][x] = oid
        elif board[y][x] == "L":
            board[y][x] = oid
            swans.append(oid)

        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= C or ny < 0 or ny >= R or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if board[ny][nx] == "X":
                ice.add((nx, ny))
                board[ny][nx] = oid
            else:
                queue.append((nx, ny))
    return ice


def find(ocean, i):
    if ocean[i] == i:
        return i
    else:
        ocean[i] = find(ocean, ocean[i])
        return ocean[i]


def union(ocean, i, j):
    i = find(ocean, i)
    j = find(ocean, j)
    if i == j:
        return
    if i < j:
        ocean[j] = i
    else:
        ocean[i] = j


def solution(R, C, board):
    visited = [[False] * C for _ in range(R)]
    queue, swans = deque([]), []
    oid = 0
    for y in range(R):
        for x in range(C):
            if board[y][x] == "." or board[y][x] == "L":
                queue.extend(bfs(R, C, board, visited, oid, x, y, swans))
                oid += 1

    ocean = [i for i in range(oid)]
    date = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for (dx, dy) in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= C or ny < 0 or ny >= R:
                    continue
                if board[ny][nx] == "X":
                    if visited[ny][nx]:
                        continue
                    visited[ny][nx] = True
                    board[ny][nx] = board[y][x]
                    queue.append((nx, ny))
                else:
                    coid, noid = find(ocean, board[y][x]), find(ocean, board[ny][nx])
                    if coid == noid:
                        continue
                    union(ocean, board[y][x], board[ny][nx])
                    if find(ocean, swans[0]) == find(ocean, swans[1]):
                        if board[y][x] < board[ny][nx]:
                            return date
                        else:
                            return date + 1
        date += 1


IR, IC = map(int, sys.stdin.readline().split())
IBoard = [list(sys.stdin.readline().rstrip()) for _ in range(IR)]
print(solution(IR, IC, IBoard))
