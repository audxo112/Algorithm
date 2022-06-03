# https://www.acmicpc.net/problem/7569
import sys


dirs = [(0, 1, 0), (-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1)]


def solution(M, N, H, board):
    queue, zero, date = [], 0, -1
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if board[z][y][x] == "0":
                    zero += 1
                elif board[z][y][x] == "1":
                    queue.append((x, y, z))
    while queue:
        date += 1
        tmp = []
        for x, y, z in queue:
            for (dx, dy, dz) in dirs:
                nx, ny, nz = x + dx, y + dy, z + dz
                if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H or \
                        board[nz][ny][nx] != "0":
                    continue
                board[nz][ny][nx] = "1"
                tmp.append((nx, ny, nz))
        zero -= len(tmp)
        queue = tmp
    return -1 if zero else date


IM, IN, IH = map(int, sys.stdin.readline().split())
IBoard = [[sys.stdin.readline().split() for _ in range(IN)] for _ in range(IH)]
print(solution(IM, IN, IH, IBoard))
