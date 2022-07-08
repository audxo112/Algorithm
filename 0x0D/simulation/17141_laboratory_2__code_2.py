# https://www.acmicpc.net/problem/17141
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def back_tacking(N, M, n=0, selected=[]):
    m = len(selected)
    if M == m:
        return [selected[:]]

    arr = []
    for i in range(n, N):
        if N - i < M - m:
            continue

        selected.append(i)
        arr += back_tacking(N, M, i + 1, selected)
        selected.pop()
    return arr


def bfs(N, board, visited, sx, sy, idx):
    queue = deque([(sx, sy)])
    visited[(sx, sy)][idx] = 0
    time = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx] or visited[(nx, ny)][idx] != 9999:
                    continue
                visited[(nx, ny)][idx] = time
                queue.append((nx, ny))
        time += 1


def simulation(virus, pos_logs, best):
    max_val = 0
    for logs in pos_logs:
        min_val = 9999
        for v in virus:
            if min_val > logs[v]:
                min_val = logs[v]
        if min_val >= best:
            return best
        elif min_val > max_val:
            max_val = min_val
    return max_val


def solution(N, M, board):
    pos = [(x, y) for y in range(N) for x in range(N) if board[y][x] == 2]
    PN = len(pos)
    visited = {}
    for y in range(N):
        for x in range(N):
            if board[y][x] == 2:
                board[y][x] = 0
                visited[(x, y)] = [9999] * PN
            elif not board[y][x]:
                visited[(x, y)] = [9999] * PN

    for idx, (x, y) in enumerate(pos):
        bfs(N, board, visited, x, y, idx)

    pos_logs = list(visited.values())
    answer = 9999
    for virus in back_tacking(len(pos), M):
        answer = simulation(virus, pos_logs, answer)

    return answer if answer != 9999 else -1


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IM, IBoard))
