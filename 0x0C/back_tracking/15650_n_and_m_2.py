# https://www.acmicpc.net/problem/15650
import sys


def back_tracking(N, M, n, m, visited):
    if M == m:
        print(" ".join(map(str, visited)))
        return

    for i in range(n, N + 1):
        visited.append(i)
        back_tracking(N, M, i + 1, m + 1, visited)
        visited.pop()


def solution(N, M):
    back_tracking(N, M, 1, 0, [])


IN, IM = map(int, sys.stdin.readline().split())
solution(IN, IM)
