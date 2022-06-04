# https://www.acmicpc.net/problem/7569
import sys
from collections import deque


def solution(N, K):
    if N == K:
        return 0

    visited = [[False] * 500001 for _ in range(2)]
    visited[0][N] = True
    queue = deque([N])
    t, tmp = 0, 0
    while queue:
        K += (t := t + 1)
        if K > 500000:
            return -1
        if visited[t % 2][K]:
            return t

        for _ in range(len(queue)):
            n = queue.popleft()
            for nn in [n - 1, n + 1, n * 2]:
                if nn < 0 or nn > 500000 or visited[t % 2][nn]:
                    continue
                if nn == K:
                    return t
                visited[t % 2][nn] = True
                queue.append(nn)
    return -1


IN, IK = map(int, sys.stdin.readline().split())
print(solution(IN, IK))
