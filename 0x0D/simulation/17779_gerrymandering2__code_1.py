# https://www.acmicpc.net/problem/17779
import sys


def simulation(N, A, sx, sy, d1, d2):
    people = [0] * 5
    for y in range(N):
        for x in range(N):
            if x <= sx + d1 and y < sy and x + y < sx + sy:
                people[0] += A[y][x]
            elif x > sx + d1 and y <= sy - d1 + d2 and x - y > sx + d1 - sy + d1:
                people[1] += A[y][x]
            elif x < sx + d2 and y >= sy and x - y < sx - sy:
                people[2] += A[y][x]
            elif x >= sx + d2 and y > sy - d1 + d2 and x + y > sx + d2 + sy + d2:
                people[3] += A[y][x]
            else:
                people[4] += A[y][x]
    return max(people) - min(people)


def solution(N, A):
    answer = 40000
    d1 = d2 = 1
    while N - d1 - d2 > 0:
        for y in range(d1, N - d2):
            for x in range(1, N + 1 - d1 - d2):
                answer = min(simulation(N, A, x, y, d1, d2), answer)
        d1 += 1
        if N - d1 - d2 <= 0:
            d1 = 1
            d2 += 1
    return answer


IN = int(sys.stdin.readline())
IA = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IA))
