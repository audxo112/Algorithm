# https://www.acmicpc.net/problem/16987
import sys


def back_tracking(N, S, W, n, b):
    if N <= n:
        return b
    if S[n] <= 0:
        return back_tracking(N, S, W, n + 1, b)
    maxCnt = b
    for i in range(N):
        if i == n or S[i] <= 0:
            continue
        S[n], S[i] = S[n] - W[i], S[i] - W[n]
        maxCnt = max(back_tracking(N, S, W, n + 1, b + (S[n] <= 0) + (S[i] <= 0)), maxCnt)
        S[n], S[i] = S[n] + W[i], S[i] + W[n]
    return maxCnt


def solution(N, S, W):
    return back_tracking(N, S, W, 0, 0)


IN = int(sys.stdin.readline())
IS, IW = [], []
for _ in range(IN):
    Is, Iw = map(int, sys.stdin.readline().split())
    IS.append(Is)
    IW.append(Iw)
print(solution(IN, IS, IW))
