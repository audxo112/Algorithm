# https://www.acmicpc.net/problem/1759
import sys


def back_tracking(L, C, words, vowels, n, vc, visited):
    N = len(visited)
    if C - n < L - N:
        return

    if L == 0:
        if vc >= 1 and N - vc >= 2:
            print("".join(visited))
        return

    for i in range(n, C):
        visited.append(words[i])
        back_tracking(L - 1, C, words, vowels, i + 1, vc + vowels[i], visited)
        visited.pop()


def solution(L, C, words):
    vowels = [1 if word in "aeiou" else 0 for word in words]
    back_tracking(L, C, words, vowels, 0, 0, [])


IL, IC = map(int, sys.stdin.readline().split())
IWords = sorted(sys.stdin.readline().split())
solution(IL, IC, IWords)
