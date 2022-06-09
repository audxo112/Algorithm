# https://www.acmicpc.net/problem/11729
import sys


def recursion(cache, N, n_from, n_to, n_tmp):
    if N == 1:
        return f"{n_from} {n_to}\n"
    if (N, n_from, n_to) in cache:
        return cache[(N, n_from, n_to)]

    cache[(N, n_from, n_to)] = "".join([
        recursion(cache, N - 1, n_from, n_tmp, n_to),
        f"{n_from} {n_to}\n",
        recursion(cache, N - 1, n_tmp, n_to, n_from),
    ])
    return cache[(N, n_from, n_to)]


def solution(N):
    cache = dict()
    return recursion(cache, N, 1, 3, 2)


IN = int(sys.stdin.readline())
print(2**IN - 1)
print(solution(IN))
