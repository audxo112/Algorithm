# https://www.acmicpc.net/problem/17143
import sys


dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
cd = [1, 0, 3, 2]


def bound(cycle, dp, min_val, max_val, val, d):
    if val < min_val:
        mod = (min_val - val) % cycle
        return cd[d] if min_val <= mod < max_val else d, min_val + dp[mod]
    elif val > max_val:
        mod = (val - max_val) % cycle
        return cd[d] if min_val <= mod < max_val else d, max_val - dp[mod]
    return d, val


def move(R, C, RC, CC, r_dp, c_dp, sharks, x, y, s, d, z):
    dx, dy = dirs[d]
    if d > 1:
        d, x = bound(CC, c_dp, 1, C, x + s * dx, d)
    else:
        d, y = bound(RC, r_dp, 1, R, y + s * dy, d)
    if (x, y) not in sharks or z > sharks[(x, y)][2]:
        sharks[(x, y)] = (s, d, z)
    return x, y


def solution(R, C, M, info):
    RC, CC = (R - 1) * 2, (C - 1) * 2
    r_dp = [i if i < R else RC - i for i in range(RC)]
    c_dp = [i if i < C else CC - i for i in range(CC)]
    sharks = {}
    king, size = 1, 0
    cy = 101
    for y, x, s, d, z in info:
        sharks[(x, y)] = [s, d - 1, z]
        if x == king:
            cy = min(y, cy)

    while sharks:
        if cy != 101:
            size += sharks[(king, cy)][2]
            del sharks[(king, cy)]
            cy = 101

        if king == C:
            return size

        king += 1
        nxt = {}
        for (sx, sy), (s, d, z) in sharks.items():
            nx, ny = move(R, C, RC, CC, r_dp, c_dp, nxt, sx, sy, s, d, z)
            if nx == king:
                cy = min(ny, cy)
        sharks = nxt
    return size


IR, IC, IM = map(int, sys.stdin.readline().split())
IInfo = [map(int, sys.stdin.readline().split()) for _ in range(IM)]
print(solution(IR, IC, IM, IInfo))
