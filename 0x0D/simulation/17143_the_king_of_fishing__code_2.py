# https://www.acmicpc.net/problem/17143
import sys


dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
cd = [1, 0, 3, 2]


def simulation(R, C, RC, CC, sharks):
    nxt = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if sharks[y][x]:
                s, d, z = sharks[y][x]
                dx, dy = dirs[d]
                nx, ny = x + s * dx, y + s * dy
                if nx < 0:
                    d, nx = cd[d], -nx
                elif nx >= C:
                    d, nx = cd[d], CC - nx
                elif ny < 0:
                    d, ny = cd[d], -ny
                elif ny >= R:
                    d, ny = cd[d], RC - ny

                if not nxt[ny][nx] or z > nxt[ny][nx][2]:
                    nxt[ny][nx] = [s, d, z]
    return nxt


def solution(R, C, M, info):
    RC, CC = (R - 1) * 2, (C - 1) * 2
    sharks = [[0] * C for _ in range(R)]
    king, size = 0, 0
    for y, x, s, d, z in info:
        x, y, d = x - 1, y - 1, d - 1
        l, c = (C, CC) if d > 1 else (R, RC)
        s %= c
        if s >= l:
            s = c - s
            d = cd[d]
        sharks[y][x] = [s, d, z]

    while sharks:
        for y in range(R):
            if sharks[y][king]:
                size += sharks[y][king][2]
                sharks[y][king] = 0
                break

        if king == C - 1:
            return size

        king += 1
        sharks = simulation(R, C, RC, CC, sharks)
    return size


IR, IC, IM = map(int, sys.stdin.readline().split())
IInfo = [map(int, sys.stdin.readline().split()) for _ in range(IM)]
print(solution(IR, IC, IM, IInfo))
