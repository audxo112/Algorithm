# https://www.acmicpc.net/problem/16235
import sys
from collections import defaultdict, deque


def move(N, x, y):
    if x > 0:
        yield x - 1, y
        if y > 0:
            yield x - 1, y - 1
        if y < N - 1:
            yield x - 1, y + 1
    if x < N - 1:
        yield x + 1, y
        if y > 0:
            yield x + 1, y - 1
        if y < N - 1:
            yield x + 1, y + 1
    if y > 0:
        yield x, y - 1
    if y < N - 1:
        yield x, y + 1


def solution(N, M, K, A, info):
    foods = [[5] * N for _ in range(N)]
    trees = defaultdict(deque)

    for y, x, age in info:
        trees[(x - 1, y - 1)].append(age)

    for k in range(K):
        breeding = defaultdict(int)
        for (x, y), tl in trees.items():
            exist = True
            for _ in range(len(tl)):
                tree = tl.popleft()
                exist = exist and tree <= foods[y][x]
                if exist:
                    foods[y][x] -= tree
                    tl.append(tree + 1)
                    if (tree + 1) % 5 == 0:
                        breeding[(x, y)] += 1
                else:
                    foods[y][x] += tree // 2

        for key in breeding.keys():
            x, y = key
            for nxt in move(N, x, y):
                trees[nxt].extendleft([1] * breeding[key])

        for y in range(N):
            foods[y] = [a + b for a, b in zip(foods[y], A[y])]

    return sum([len(trees[t]) for t in trees])


IN, IM, IK = map(int, sys.stdin.readline().split())
IA = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
IInfo = [list(map(int, sys.stdin.readline().split())) for _ in range(IM)]
print(solution(IN, IM, IK, IA, IInfo))
