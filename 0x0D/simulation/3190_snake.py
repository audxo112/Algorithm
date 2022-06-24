# https://www.acmicpc.net/problem/3190
import sys


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(N, K, apples, L, xs, cs):
    exist = [[-2] * N for _ in range(N)]
    for ax, ay in apples:
        exist[ay][ax] = -4

    x = y = dr = idx = 0
    sl = time = 1
    exist[y][x] = 0

    while True:
        dx, dy = dirs[dr]
        x, y = x + dx, y + dy
        if x < 0 or x >= N or y < 0 or y >= N or exist[y][x] >= time - sl:
            return time
        if exist[y][x] == -4:
            sl += 1
        exist[y][x] = time
        if idx < L and time == xs[idx]:
            dr = (dr + cs[idx]) % 4
            idx += 1
        time += 1


IN = int(sys.stdin.readline())
IK = int(sys.stdin.readline())
IApples = []
for _ in range(IK):
    IR, IC = map(int, sys.stdin.readline().split())
    IApples.append((IC - 1, IR - 1))
IL = int(sys.stdin.readline())
IXS, ICS = [], []
for _ in range(IL):
    IX, IC = sys.stdin.readline().split()
    IXS.append(int(IX))
    ICS.append(3 if IC == "L" else 1)
print(solution(IN, IK, IApples, IL, IXS, ICS))
