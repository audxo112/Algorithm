# https://www.acmicpc.net/problem/1697
import sys
from collections import deque


def solution(N, K):
    if N == K:
        return 0

    queue, visited = deque([(N, 0)]), {N}
    while queue:
        n, step = queue.popleft()

        for nn in [n * 2, n + 1, n - 1]:
            if nn < 0 or nn > 100000 or nn in visited:
                continue
            if nn == K:
                return step + 1
            visited.add(nn)
            queue.append((nn, step + 1))


IN, IK = map(int, sys.stdin.readline().split())
print(solution(IN, IK))