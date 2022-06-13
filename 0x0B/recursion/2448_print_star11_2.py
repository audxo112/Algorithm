# https://www.acmicpc.net/problem/2448
import sys


def solution(N):
    if N == 3:
        return ["  *  ", " * * ", "*****"]

    nn = N // 2
    star = []
    sub = solution(nn)
    for i in range(nn):
        star.append(f'{" " * nn}{sub[i]}{" " * nn}')
    for i in range(nn):
        star.append(f'{sub[i]} {sub[i]}')
    return star


IN = int(sys.stdin.readline())
print("\n".join(solution(IN)))
