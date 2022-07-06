# https://www.acmicpc.net/problem/17140
import sys
from collections import defaultdict


def operation(array):
    nums = defaultdict(int)
    for num in array:
        if num:
            nums[num] += 1
    return sum(map(list, sorted(nums.items(), key=lambda x: (x[1], x[0]))), [])[:100]


def simulation(N, M, array):
    m = M
    for y in range(N):
        array[y] = operation(array[y])
        m = max(len(array[y]), m)
    for y in range(N):
        if len(array[y]) < m:
            array[y] += [0] * (m - len(array[y]))


def solution(R, C, K, array):
    for time in range(101):
        N, M = len(array), len(array[0])
        if N >= R and M >= C:
            if array[R - 1][C - 1] == K:
                return time

        if N >= M:
            simulation(N, M, array)
        else:
            array = list(map(list, zip(*array)))
            simulation(M, N, array)
            array = list(map(list, zip(*array)))
    return -1


IR, IC, IK = map(int, sys.stdin.readline().split())
IArray = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
print(solution(IR, IC, IK, IArray))
