# https://www.acmicpc.net/problem/3197
import sys


dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def solution(R, C, board):
    visited = [[False] * C for _ in range(R)]
    queue, squeue = [], []
    for y in range(R):
        for x in range(C):
            if board[y][x] == ".":
                queue.append((x, y))
            if board[y][x] == "L":
                board[y][x] = "."
                queue.append((x, y))
                squeue.append((x, y))
    sx, sy = squeue.pop()

    date = 1
    while queue:
        nxt_q, nxt_sq = [], []
        for x, y in queue:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= C or ny < 0 or ny >= R:
                    continue
                if board[ny][nx] == "X":
                    board[ny][nx] = "."
                    nxt_q.append((nx, ny))
        queue = nxt_q

        for x, y in squeue:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= C or ny < 0 or ny >= R or visited[ny][nx]:
                    continue
                if (nx, ny) == (sx, sy):
                    return date
                visited[ny][nx] = True
                if board[ny][nx] == ".":
                    squeue.append((nx, ny))
                elif board[ny][nx] == "X":
                    nxt_sq.append((nx, ny))
        squeue = nxt_sq
        date += 1
    return date


IR, IC = map(int, sys.stdin.readline().split())
IBoard = [list(sys.stdin.readline().rstrip()) for _ in range(IR)]
print(solution(IR, IC, IBoard))
