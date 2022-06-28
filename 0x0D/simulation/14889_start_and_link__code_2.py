# https://www.acmicpc.net/problem/14889
import sys


def back_tracking(N, M, stat, n, a_val, all_val, m_val):
    if M == 0:
        return min(abs(all_val - a_val), m_val)
    if N - n < M:
        return m_val

    for i in range(n, N):
        m_val = back_tracking(N, M - 1, stat, i + 1, a_val + stat[i], all_val, m_val)
        if m_val == 0:
            return 0

    return m_val


def solution(N, stat):
    stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
    return back_tracking(N, N // 2, stat, 0, 0, sum(stat) // 2, 1e9)


IN = int(sys.stdin.readline())
IStat = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IStat))
