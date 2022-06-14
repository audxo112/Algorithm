# https://www.acmicpc.net/problem/1182
import sys


def back_tracking(N, S, C, index, nums, total):
    if N == C:
        return 1 if total == S else 0

    cnt = 0
    for i in range(index, len(nums)):
        cnt += back_tracking(N, S, C + 1, i + 1, nums, total + nums[i])
    return cnt


def solution(N, S, nums):
    cnt = 0
    for i in range(1, N + 1):
        cnt += back_tracking(i, S, 0, 0, nums, 0)
    return cnt


IN, IS = map(int, sys.stdin.readline().split())
INums = list(map(int, sys.stdin.readline().split()))
print(solution(IN, IS, INums))
