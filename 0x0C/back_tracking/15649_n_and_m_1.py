# https://www.acmicpc.net/problem/15649
import sys


def back_tracking(N, M, visited):
    if M == 0:
        print(" ".join(map(str, visited)))
        return

    for i in range(1, N + 1):
        if i not in visited:
            visited.append(i)
            back_tracking(N, M - 1, visited)
            visited.pop()


def solution(N, M):
    back_tracking(N, M, [])


IN, IM = map(int, sys.stdin.readline().split())
solution(IN, IM)
