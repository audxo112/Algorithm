# https://www.acmicpc.net/problem/4991
import sys
from collections import deque


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def back_tracking(M, m, x, dist, visited, min_val, answer):
    if M == m:
        return min(min_val, answer)
    elif min_val >= answer:
        return answer

    for i in range(1, M):
        if visited[i]:
            continue
        visited[i] = True
        answer = back_tracking(M, m + 1, i, dist, visited, min_val + dist[x][i], answer)
        visited[i] = False
    return answer


def bfs(W, H, board, pos, sx, sy):
    visited = [[False] * W for _ in range(H)]
    visited[sy][sx] = True
    dist = [-1] * len(pos)

    queue = deque([(sx, sy)])
    cnt = time = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= W or ny < 0 or ny >= H or visited[ny][nx] or board[ny][nx] == 1:
                    continue
                visited[ny][nx] = True
                queue.append((nx, ny))

                if board[ny][nx] == -1:
                    dist[pos.index((nx, ny))] = time
                    cnt += 1
        time += 1
    if cnt == len(pos):
        return dist
    else:
        return False


def solution(W, H, board):
    pos = []
    target = []
    for y in range(H):
        for x in range(W):
            if board[y][x] == "x":
                board[y][x] = 1
            elif board[y][x] == "o":
                board[y][x] = -1
                pos.append((x, y))
            elif board[y][x] == "*":
                board[y][x] = -1
                target.append((x, y))
            else:
                board[y][x] = 0
    pos.extend(target)
    PN = len(pos)
    dist = [[] for _ in range(PN)]
    for i, (x, y) in enumerate(pos):
        dist[i] = bfs(W, H, board, pos, x, y)
        if not dist[i]:
            return -1

    visited = [False] * PN
    min_val = 4000
    for i in range(1, PN):
        visited[i] = True
        min_val = back_tracking(PN, 2, i, dist, visited, dist[0][i], min_val)
        visited[i] = False
    return min_val


total = 0
while True:
    IW, IH = map(int, sys.stdin.readline().split())
    if not IW or not IH:
        break
    IBoard = [list(sys.stdin.readline().rstrip()) for _ in range(IH)]
    print(solution(IW, IH, IBoard))
