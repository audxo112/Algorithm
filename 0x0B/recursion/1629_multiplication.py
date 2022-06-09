# https://www.acmicpc.net/problem/1629
import sys


def recursion(A, B, C):
    B, m = divmod(B, 2)
    r = A * m % C if m else 1
    return r * recursion(A ** 2 % C, B, C) % C if B else r


def solution(A, B, C):
    return recursion(A, B, C)


IA, IB, IC = map(int, sys.stdin.readline().split())
print(solution(IA, IB, IC))
