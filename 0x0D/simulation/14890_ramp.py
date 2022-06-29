# https://www.acmicpc.net/problem/14890
import sys


def simulation(N, L, road):
    ramp = [False] * N
    for i in range(N - 1):
        if road[i] == road[i + 1]:
            continue
        if road[i] - road[i + 1] == 1:
            left, right = i + 1, i + L + 1
            if right > N or road[left:right].count(road[i + 1]) != L or True in ramp[left:right]:
                return 0
            ramp[left:right] = [True] * L
        elif road[i + 1] - road[i] == 1:
            left, right = i - L + 1, i + 1
            if left < 0 or road[left:right].count(road[i]) != L or True in ramp[left:right]:
                return 0
            ramp[left:right] = [True] * L
        else:
            return 0
    return 1


def solution(N, L, board):
    cnt = 0
    for road in board:
        cnt += simulation(N, L, road)
    for road in zip(*board):
        cnt += simulation(N, L, road)
    return cnt


IN, IL = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IL, IBoard))
