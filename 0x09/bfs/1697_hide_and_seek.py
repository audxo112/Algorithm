# https://www.acmicpc.net/problem/1697
import sys
from collections import deque

IN, IK = map(int, sys.stdin.readline().split())


def solution(N, K):
    visited = set()
    if N == K:
        return 0

    queue = deque([(N, 0)])
    while queue:
        n, step = queue.popleft()
        if n * 2 == K or n + 1 == K or n - 1 == K:
            return step + 1
        if 0 <= n * 2 <= 100000 and n * 2 not in visited:
            visited.add(n * 2)
            queue.append((n * 2, step + 1))
        if 0 <= n + 1 <= 100000 and n + 1 not in visited:
            visited.add(n + 1)
            queue.append((n + 1, step + 1))
        if 0 <= n - 1 <= 100000 and n - 1 not in visited:
            visited.add(n - 1)
            queue.append((n - 1, step + 1))


print(solution(IN, IK))

