# https://www.acmicpc.net/problem/13549
import sys
from heapq import heappop, heappush


def solution(N, K):
    if N == K:
        return 0

    visited = [False] * 100001
    visited[N] = [True]
    queue = [(0, N)]

    while queue:
        t, n = heappop(queue)
        nm = n
        while (nm := 2 * nm) <= 100000 and 0 < nm < 2 * K:
            if visited[nm]:
                continue
            if nm == K:
                return t
            visited[nm] = True
            heappush(queue, (t, nm))

        if n < K:
            dirs = [n + 1, n - 1]
        else:
            dirs = [n - 1]

        for nn in dirs:
            if nn < 0 or nn > 100000 or visited[nn]:
                continue
            if nn == K:
                return t + 1
            visited[nn] = True
            heappush(queue, (t + 1, nn))


IN, IK = map(int, sys.stdin.readline().split())
print(solution(IN, IK))