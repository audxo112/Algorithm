# https://www.acmicpc.net/problem/2839
import sys


def solution(N):
    if N == 4 or N == 7:
        return - 1
    dp = [0, 1, 2, 1, 2]
    d5, m5 = divmod(N, 5)
    return d5 + dp[m5]


IN = int(sys.stdin.readline())
print(solution(IN))
