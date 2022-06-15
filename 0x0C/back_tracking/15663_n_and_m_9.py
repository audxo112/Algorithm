# https://www.acmicpc.net/problem/15663
import sys


def back_tracking(N, M, nums, visited):
    if M == 0:
        print(" ".join(map(lambda x: nums[x], visited)))
        return

    before = ""
    for i in range(N):
        if before == nums[i] or i in visited:
            continue
        before = nums[i]
        visited.append(i)
        back_tracking(N, M - 1, nums, visited)
        visited.pop()


def solution(N, M, nums):
    back_tracking(N, M, nums, [])


IN, IM = map(int, sys.stdin.readline().split())
INums = sorted(sys.stdin.readline().split(), key=lambda x: int(x))
solution(IN, IM, INums)
