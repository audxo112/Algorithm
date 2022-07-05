# https://www.acmicpc.net/problem/16236
import sys


dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]


def simulation(N, board, visited, sx, sy, shark, fish):
    queue = [(sx, sy)]
    visited[sy][sx] = fish
    time = 0
    while queue:
        tmp = []
        for x, y in queue:
            if board[y][x] and shark > board[y][x]:
                board[y][x] = 0
                return time, x, y

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[ny][nx] == fish or board[ny][nx] > shark:
                    continue

                visited[ny][nx] = fish
                tmp.append((nx, ny))
        queue = sorted(tmp, key=lambda p: (p[1], p[0]))
        time += 1

    return 0, sx, sy


def solution(N, board):
    sx = sy = fish = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 9:
                sx, sy = x, y
                board[y][x] = 0
            elif board[y][x]:
                fish += 1
    if fish == 0:
        return 0

    shark, e_cnt, time = 2, 0, 0
    visited = [[fish + 1] * N for _ in range(N)]
    while fish:
        t, sx, sy = simulation(N, board, visited, sx, sy, shark, fish)
        if not t:
            return time

        time, fish, e_cnt = time + t, fish - 1, e_cnt + 1
        if e_cnt == shark:
            shark += 1
            e_cnt = 0
    return time


IN = int(sys.stdin.readline())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IBoard))
