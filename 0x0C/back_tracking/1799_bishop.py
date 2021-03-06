# https://www.acmicpc.net/problem/1799
import sys
from collections import defaultdict


def back_tracking(N, pos, m_slop, p_slop, n, empty=0):
    if N <= n:
        return n // 2 - empty
    cnt = place = 0
    if pos[n]:
        for x, y in pos[n]:
            if not m_slop[x + y] and not p_slop[x - y]:
                m_slop[x + y] = p_slop[x - y] = True
                cnt = max(back_tracking(N, pos, m_slop, p_slop, n + 2, empty), cnt)
                m_slop[x + y] = p_slop[x - y] = False
            else:
                place += 1
        if len(pos[n]) == place:
            cnt = max(back_tracking(N, pos, m_slop, p_slop, n + 2, empty + 1), cnt)
    else:
        cnt = max(back_tracking(N, pos, m_slop, p_slop, n + 2, empty + 1), cnt)
    return cnt


def solution(N, board):
    m_slop = [False] * (2 * N - 1)
    p_slop = [False] * (2 * N - 1)
    pos = defaultdict(list)
    for x, y in [(x, y) for x in range(N) for y in range(N)]:
        if board[y][x] == "1":
            pos[x + y].append((x, y))
    return back_tracking(2 * N - 1, pos, m_slop, p_slop, 0) + back_tracking(2 * N - 1, pos, m_slop, p_slop, 1)


IN = int(sys.stdin.readline())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
print(solution(IN, IBoard))
