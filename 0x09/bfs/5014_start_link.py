# https://www.acmicpc.net/problem/5014
import sys
from collections import deque


def solution(F, S, G, U, D):
    visited = [False] * (F + 1)
    queue = deque([(S, 0)])
    visited[S] = True

    while queue:
        floor, cnt = queue.popleft()
        if floor == G:
            return cnt

        for nf in (floor + U, floor - D):
            if nf < 1 or nf > F or visited[nf]:
                continue
            visited[nf] = True
            queue.append((nf, cnt + 1))
    return "use the stairs"


IF, IS, IG, IU, ID = map(int, sys.stdin.readline().split())
print(solution(IF, IS, IG, IU, ID))

