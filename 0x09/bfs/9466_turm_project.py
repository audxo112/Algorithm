import sys


def search(graph, sn):
    n_set, n = {sn}, sn

    while True:
        n = graph[n]
        if n == sn or not graph[n]:
            for v in n_set:
                graph[v] = 0
            return len(n_set) if n == sn else 0
        if n in n_set:
            return search(graph, n)
        n_set.add(n)


def solution(N, graph):
    cnt = N
    for i in range(1, N + 1):
        if graph[i]:
            cnt -= search(graph, i)
    return cnt


for _ in range(int(sys.stdin.readline())):
    IN = int(sys.stdin.readline())
    IGraph = [0] + list(map(int, sys.stdin.readline().split()))
    print(solution(IN, IGraph))
