# https://www.acmicpc.net/problem/13335
import sys
from collections import deque


def solution(N, W, L, trucks):
    entered = deque()
    time = l = 0
    for i, truck in enumerate(trucks):
        while truck + l > L:
            o_truck, e_time = entered.popleft()
            time = max(e_time + W - 1, time)
            l -= o_truck
        time += 1
        l += truck
        entered.append((truck, time))
    if entered:
        time = entered[-1][1] + W

    return time


IN, IW, IL = map(int, sys.stdin.readline().split())
ITrucks = list(map(int, sys.stdin.readline().split()))
print(solution(IN, IW, IL, ITrucks))
