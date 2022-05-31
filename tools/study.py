import sys
sys.setrecursionlimit(1500000)
from collections import defaultdict
import heapq as hq


def solution(n, paths, gates, summits):
    N = 0
    G = 1
    S = 2

    def nodetype(node):
        if node in gates:
            return G
        elif node in summits:
            return S
        return N

    graph = defaultdict(list)
    for (src, dst, inten) in paths:
        hq.heappush(graph[src], (inten, dst, nodetype(dst)))
        hq.heappush(graph[dst], (inten, src, nodetype(src)))

    answer = [0, 100000007]

    def dfs(s, inten, mInten, visited):
        lst = graph[s][:]

        while lst:
            cInten, cn, ct = hq.heappop(lst)
            if inten >= visited[cn] or ct == G or cInten >= mInten:
                continue
            nInten = max(inten, cInten)
            visited[cn] = nInten
            if ct == S:
                if answer[1] > nInten or (answer[1] == nInten and answer[0] > cn):
                    answer[0] = cn
                    answer[1] = nInten
                return
            dfs(cn, nInten, mInten, visited)

    for g in gates:
        visited = [100000007] * (n + 1)
        visited[g] = 0
        dfs(g, 0, answer[1], visited)
    return answer


# print(solution(6, 	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, 		[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))