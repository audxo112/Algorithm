# https://www.acmicpc.net/problem/15650
import sys


def back_tracking(N, M, n, visited):
    if M == 0:
        print(" ".join(map(str, visited)))
        return

    for i in range(n, N + 1):
        visited.append(i)
        back_tracking(N, M - 1, i + 1, visited)
        visited.pop()


def solution(N, M):
    back_tracking(N, M, 1, [])


IN, IM = map(int, sys.stdin.readline().split())
solution(IN, IM)
