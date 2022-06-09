# https://www.acmicpc.net/problem/9328
import sys
from collections import deque, defaultdict


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def process(board, visited, queue, door, key, sx, sy):
    c = board[sy][sx]
    if c == ".":
        visited[sy][sx] = 2
        queue.append((sx, sy))
    elif c == "$":
        visited[sy][sx] = 2
        queue.append((sx, sy))
        return 1
    elif c.islower():
        key[c.upper()] = c
        visited[sy][sx] = 2
        queue.append((sx, sy))
        for (dx, dy) in door[c.upper()]:
            if visited[dy][dx] == 1:
                visited[dy][dx] = 2
                queue.append((dx, dy))
        door[c.upper()].clear()
    elif c.isupper():
        if c in key:
            visited[sy][sx] = 2
            queue.append((sx, sy))
        else:
            visited[sy][sx] = 1
            door[c].append((sx, sy))
    return 0


def solution(H, W, board, key):
    visited = [[0] * W for _ in range(H)]
    door = defaultdict(list)
    queue = deque()
    doc = 0

    for row, col in [[range(1, H - 1), (0, W - 1)], [(0, H - 1), range(W)]]:
        for y in row:
            for x in col:
                doc += process(board, visited, queue, door, key, x, y)

    while queue:
        x, y = queue.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= W or ny < 0 or ny >= H or \
                    visited[ny][nx] or board[ny][nx] == "*":
                continue
            doc += process(board, visited, queue, door, key, nx, ny)
    return doc


for _ in range(int(sys.stdin.readline())):
    IH, IW = map(int, sys.stdin.readline().split())
    IBoard = [sys.stdin.readline().rstrip() for _ in range(IH)]
    IKey = dict()
    for k in sys.stdin.readline().rstrip():
        if k != "0":
            IKey[k.upper()] = k
    print(solution(IH, IW, IBoard, IKey))
