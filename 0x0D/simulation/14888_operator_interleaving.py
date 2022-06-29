# https://www.acmicpc.net/problem/14888
import sys


def cal(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return abs(num1) // num2 * -1
        else:
            return num1 // num2


def back_tracking(N, nums, ops, n, num, max_val, min_val):
    if N == n:
        return max(num, max_val), min(num, min_val)

    for i in range(4):
        if not ops[i]:
            continue
        ops[i] -= 1
        max_val, min_val = back_tracking(N, nums, ops, n + 1, cal(num, nums[n], i), max_val, min_val)
        ops[i] += 1
    return max_val, min_val


def solution(N, nums, ops):
    return back_tracking(N, nums, ops, 1, nums[0], -1e9, 1e9)


IN = int(sys.stdin.readline())
INums = list(map(int, sys.stdin.readline().split()))
IOps = list(map(int, sys.stdin.readline().split()))
for OAns in solution(IN, INums, IOps):
    print(OAns)
