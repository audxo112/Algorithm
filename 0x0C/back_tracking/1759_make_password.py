# https://www.acmicpc.net/problem/1759
import sys


def back_tracking(L, C, words, vowels, n, vc, visited):
    if L == 0:
        if vc >= 1 and len(visited) - vc >= 2:
            print("".join(visited))
        return

    for i in range(n, C):
        visited.append(words[i])
        back_tracking(L - 1, C, words, vowels, i + 1, vc + vowels[i], visited)
        visited.pop()


def solution(L, C, words):
    vowels = [0] * C
    for i, c in enumerate(words):
        if c in "aeiou":
            vowels[i] = 1
    back_tracking(L, C, words, vowels, 0, 0, [])


IL, IC = map(int, sys.stdin.readline().split())
IWords = sorted(sys.stdin.readline().split())
solution(IL, IC, IWords)