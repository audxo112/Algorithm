# https://www.acmicpc.net/problem/17142
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def back_tracking(N, M, n, pos, selected):
    m = len(selected)
    if M == m:
        return [selected[:]]
    arr = []
    for i in range(n, N):
        if N - i < M - m:
            continue
        selected.append(pos[i])
        arr += back_tracking(N, M, i + 1, pos, selected)
        selected.pop()
    return arr


def bfs(N, board, virus, zero):
    visited = [[False] * N for _ in range(N)]
    for vx, vy in virus:
        visited[vy][vx] = True
    queue = deque(virus)
    time = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[ny][nx] or board[ny][nx] == 1:
                    continue
                visited[ny][nx] = True
                queue.append((nx, ny))
                if not board[ny][nx]:
                    zero -= 1
        time += 1
        if zero == 0:
            return time
    return 0


def solution(N, M, board):
    pos = [(x, y) for x in range(N) for y in range(N) if board[y][x] == 2]
    zero = N * N - sum(sum(board, [])) + len(pos)
    if zero == 0:
        return 0

    min_val = 1000000
    for virus in back_tracking(len(pos), M, 0, pos, []):
        if result := bfs(N, board, virus, zero):
            min_val = min(result, min_val)
    return min_val if min_val != 1000000 else -1


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IM, IBoard))
