# https://www.acmicpc.net/problem/15655
import sys


def back_tracking(N, M, nums, n, visited):
    if N < n:
        return

    if M == 0:
        print(" ".join(visited))
        return

    for i in range(n, N):
        visited.append(nums[i])
        back_tracking(N, M - 1, nums, i + 1, visited)
        visited.pop()


def solution(N, M, nums):
    back_tracking(N, M, nums, 0, [])


IN, IM = map(int, sys.stdin.readline().split())
INums = sorted(sys.stdin.readline().split(), key=lambda x: int(x))
solution(IN, IM, INums)
