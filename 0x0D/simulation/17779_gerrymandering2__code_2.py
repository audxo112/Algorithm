# https://www.acmicpc.net/problem/17779
import sys


def simulation(N, A, total, x1, y1, d1, d2):
    people = [0] * 5
    x2, y2 = x1 + d1, y1 - d1
    x3, y3 = x2 + d2, y2 + d2
    x4, y4 = x1 + d2, y1 + d2
    slop1, slop2, slop3, slop4 = x1 + y1, x2 - y2, x1 - y1, x4 + y4

    for y in range(N):
        if y < y2:
            people[0] += A[y][x2]
            people[1] += A[y][-2] - A[y][x2]
        elif y > y4:
            people[2] += A[y][x4 - 1]
            people[3] += A[y][-2] - A[y][x4 - 1]
        else:
            if y < y1:
                people[0] += A[y][slop1 - y - 1]
            else:
                people[2] += A[y][slop3 + y - 1]
            if y <= y3:
                people[1] += A[y][-2] - A[y][slop2 + y]
            else:
                people[3] += A[y][-2] - A[y][slop4 - y]

    people[4] = total - sum(people)
    return max(people) - min(people)


def solution(N, A):
    total = 0
    for y in range(N):
        for x in range(1, N):
            A[y][x] += A[y][x - 1]
        total += A[y][-1]
        A[y] = [0] + A[y] + [0]

    answer = 40000
    d1 = d2 = 1
    while N - d1 - d2 > 0:
        for y in range(d1, N - d2):
            for x in range(1, N + 1 - d1 - d2):
                answer = min(simulation(N, A, total, x, y, d1, d2), answer)
        d1 += 1
        if N - d1 - d2 <= 0:
            d1 = 1
            d2 += 1
    return answer


IN = int(sys.stdin.readline())
IA = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IA))
