# https://www.acmicpc.net/problem/17281
import sys
from itertools import permutations


def simulations(N, innings, orders):
    score = co = 0
    for ci in range(N):
        out = 0
        b1 = b2 = b3 = 0
        while out < 3:
            if innings[ci][orders[co]] == 0:
                out += 1
            elif innings[ci][orders[co]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif innings[ci][orders[co]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif innings[ci][orders[co]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif innings[ci][orders[co]] == 4:
                score += 1 + b1 + b2 + b3
                b1, b2, b3 = 0, 0, 0
            co = (co + 1) % 9
    return score


def solution(N, innings):
    ans = 0
    for order in permutations(range(1, 9), 8):
        ans = max(simulations(N, innings, list(order[:3]) + [0] + list(order[3:])), ans)
    return ans


IN = int(sys.stdin.readline())
IInnings = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IInnings))
