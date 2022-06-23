# https://www.acmicpc.net/problem/16985
import sys
from collections import deque


MIN_DIST, MAX_DIST = 12, 1000


def back_tracking(M, maze, visited):
    if M == 0:
        return bfs(list(map(lambda x: maze[x], visited)))

    dist = MAX_DIST
    for i in range(5):
        if i in visited:
            continue
        visited.append(i)
        for _ in range(4):
            maze[i] = list(map(list, zip(*maze[i][::-1])))
            if (M == 5 and maze[i][0][0] == "0") or (M == 1) and maze[i][4][4] == "0":
                continue
            dist = min(back_tracking(M - 1, maze, visited), dist)
            if dist == MIN_DIST:
                return dist
        visited.pop()
    return dist


def move(x, y, z):
    if x + 1 < 5:
        yield x + 1, y, z
    if x - 1 >= 0:
        yield x - 1, y, z
    if y + 1 < 5:
        yield x, y + 1, z
    if y - 1 >= 0:
        yield x, y - 1, z
    if z + 1 < 5:
        yield x, y, z + 1
    if z - 1 >= 0:
        yield x, y, z - 1


def bfs(maze):
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    queue = deque([(0, 0, 0)])
    dist, goal = 0, (4, 4, 4)
    while queue:
        dist += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            for nx, ny, nz in move(x, y, z):
                if visited[nz][ny][nx] or maze[nz][ny][nx] == "0":
                    continue
                if (nx, ny, nz) == goal:
                    return dist
                visited[nz][ny][nx] = True
                queue.append((nx, ny, nz))
    return MAX_DIST


def solution(maze):
    dist = back_tracking(5, maze, [])
    return dist if dist != MAX_DIST else -1


IMaze = [[sys.stdin.readline().split() for _ in range(5)] for _ in range(5)]
print(solution(IMaze))
