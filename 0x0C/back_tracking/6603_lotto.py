# https://www.acmicpc.net/problem/6603
import sys


def back_tracking(N, M, nums, n, visited):
    if M == 0:
        print(" ".join(visited))
        return

    for i in range(n, N):
        visited.append(nums[i])
        back_tracking(N, M - 1, nums, i + 1, visited)
        visited.pop()


def solution(N, nums):
    back_tracking(N, 6, nums, 0, [])
    print()


while True:
    IInput = sys.stdin.readline().split()
    if IInput[0] == "0":
        break
    IN, INums = int(IInput[0]), IInput[1:]
    solution(IN, INums)

