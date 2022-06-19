# https://www.acmicpc.net/problem/15683
import sys


dirs = {
    "1": [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]],
    "2": [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    "3": [[(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)]],
    "4": [[(1, 0), (0, 1), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(-1, 0), (0, -1), (0, 1)], [(-1, 0), (0, 1), (1, 0)]],
    "5": [[(1, 0), (0, 1), (0, -1), (-1, 0)]],
}


def watch(N, M, board, visited, x, y, dr, val):
    dx, dy = dr
    while 0 <= x < M and 0 <= y < N:
        if board[y][x] == "6":
            break
        visited[y][x] += val
        x, y = x + dx, y + dy


def back_tracking(N, M, board, visited, pos, i):
    if len(pos) == i:
        return sum([v.count(0) for v in visited])

    empty = N * M
    x, y = pos[i]
    for drs in dirs[board[y][x]]:
        for dr in drs:
            watch(N, M, board, visited, x, y, dr, 1)
        empty = min(back_tracking(N, M, board, visited, pos, i + 1), empty)
        for dr in drs:
            watch(N, M, board, visited, x, y, dr, -1)
    return empty


def solution(N, M, board):
    visited = [[0] * M for _ in range(N)]
    pos = []
    for y in range(N):
        for x in range(M):
            if board[y][x] == "6":
                visited[y][x] = 1
            elif board[y][x] != "0":
                pos.append((x, y))
    return back_tracking(N, M, board, visited, pos, 0)


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
print(solution(IN, IM, IBoard))
