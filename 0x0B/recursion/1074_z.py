# https://www.acmicpc.net/problem/1074
import sys


def recursion(N, r, c):
    if N == 1:
        return r * 2 + c

    nn = 2 ** (N - 1)
    rn, r = divmod(r, nn)
    cn, c = divmod(c, nn)

    return nn * nn * (rn * 2 + cn) + recursion(N - 1, r, c)


def solution(N, r, c):
    return recursion(N, r, c)


IN, IR, IC = map(int, sys.stdin.readline().split())
print(solution(IN, IR, IC))