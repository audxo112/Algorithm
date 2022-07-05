# https://www.acmicpc.net/problem/17071
import sys
from collections import deque


def solution(N, K):
    if N == K:
        return 0

    # 수빈이가 방문한 지점을 저장을 하는데 홀수 시간 인지 짝수 시간 인지를 저장 한다
    # 수빈이가 +1 -1을 각각 1번씩 실행하게 되면 같은 위치게 오게되고
    # 동생이 그 지점을 밟게 되면 동생과 수빈이가 만나는 시간이된다
    # visited 의 경우 수빈이가 밟을때 저장을 하기 때문에
    # 무조건 동생이 밟은 시점보다 이전이다

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
                # 지난 시간기준 짝, 홀을 고려하여 밟은적 있는지를 저장한다
                visited[t % 2][nn] = True
                queue.append(nn)
    return -1


IN, IK = map(int, sys.stdin.readline().split())
print(solution(IN, IK))
