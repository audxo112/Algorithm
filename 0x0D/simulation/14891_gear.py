# https://www.acmicpc.net/problem/14891
import sys


def rotate(gears, i, left, right, dr):
    gear = gears[i]
    if left and gear[-2] != left[2]:
        rotate(gears, i - 1, gears[i - 2], "", dr * -1)
    if right and gear[2] != right[-2]:
        rotate(gears, i + 1, "", gears[i + 2], dr * - 1)
    gears[i] = gear[1:] + gear[0] if dr < 0 else gear[-1] + gear[:-1]


def solution(gears, K, rotates):
    for num, dr in rotates:
        rotate(gears, num, gears[num - 1], gears[num + 1], dr)
    return sum(map(lambda g: int(g[1][0]) * 2 ** g[0], enumerate(gears[1:-1])))


IGears = [""] + [sys.stdin.readline().rstrip() for _ in range(4)] + [""]
IK = int(sys.stdin.readline())
IRotates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(IK)]
print(solution(IGears, IK, IRotates))
