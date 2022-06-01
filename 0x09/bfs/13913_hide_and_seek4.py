# https://www.acmicpc.net/problem/13913
import sys
from collections import deque


def get_history(N, K, visited):
    history = deque()
    h = K
    while h != N:
        history.appendleft(h)
        h = visited[h]
    history.appendleft(N)
    return history


def solution(N, K):
    if N == K:
        return [N]
    elif N > K:
        return range(N, K - 1, -1)
    elif K * 3 / 4 < N < K:
        return range(N, K + 1)

    visited = [-1] * 100001
    visited[N] = True
    queue = deque([N])
    while queue:
        n = queue.popleft()
        dirs = [n - 1] if n > K else [n * 2] if n > 0 and K % (2 * n) == 0 else [n - 1, n + 1, n * 2]
        for nn in dirs:
            if nn < 0 or nn > 100000 or visited[nn] != -1:
                continue
            visited[nn] = n
            if nn == K:
                return get_history(N, K, visited)
            queue.append(nn)


IN, IK = map(int, sys.stdin.readline().split())
OAnswer = solution(IN, IK)
print(len(OAnswer) - 1)
print(' '.join(map(str, OAnswer)))
