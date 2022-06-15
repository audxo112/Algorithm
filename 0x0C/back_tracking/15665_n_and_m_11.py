# https://www.acmicpc.net/problem/15665
import sys


def back_tracking(N, M, nums, visited):
    if M == 0:
        print(" ".join(visited))
        return

    for i in range(N):
        visited.append(nums[i])
        back_tracking(N, M - 1, nums, visited)
        visited.pop()


def solution(N, M, nums):
    back_tracking(N, M, nums, [])


IN, IM = map(int, sys.stdin.readline().split())
INums = sorted(set(sys.stdin.readline().split()), key=lambda x: int(x))
solution(len(INums), IM, INums)
