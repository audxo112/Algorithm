# https://www.acmicpc.net/problem/15654
import sys


def back_tracking(N, M, nums, visited):
    if M == 0:
        print(" ".join(visited))
        return

    for num in nums:
        if num in visited:
            continue
        visited.append(num)
        back_tracking(N, M - 1, nums, visited)
        visited.pop()


def solution(N, M, nums):
    back_tracking(N, M, nums, [])


IN, IM = map(int, sys.stdin.readline().split())
INums = sorted(sys.stdin.readline().split(), key=lambda x: int(x))
solution(IN, IM, INums)
