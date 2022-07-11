# https://www.acmicpc.net/problem/16986
import sys


def simulation(A, GM, o, gmo, z):
    no, gm, gmo[o] = (o + 1) % 2, GM[o][gmo[o]], (gmo[o] + 1) % 20
    if A[z][gm] == 2:
        return 1, 0, 0, no, gmo
    else:
        gm, ngm = GM[o][gmo[o]], GM[no][gmo[no]]
        gmo[o], gmo[no] = (gmo[o] + 1) % 20, (gmo[no] + 1) % 20
        if o == 0:
            if A[gm][ngm] == 2:
                return 0, 2, 0, o, gmo
            else:
                return 0, 1, 1, no, gmo
        else:
            if A[gm][ngm] >= 1:
                return 0, 0, 2, o, gmo
            else:
                return 0, 1, 1, no, gmo


def back_tracking(N, n, K, A, GM, o, gmo, visited, wz, wg, wm):
    if wz >= K:
        return 1
    elif N == n or N - n < K - wz or wg >= K or wm >= K:
        return 0

    for z in range(N):
        if visited[z]:
            continue
        visited[z] = True
        nz, ng, nm, no, ngmo = simulation(A, GM, o, gmo[:], z)
        if back_tracking(N, n + 1, K, A, GM, no, ngmo, visited, wz + nz, wg + ng, wm + nm):
            return 1
        visited[z] = False
    return 0


def solution(N, K, A, GM):
    if N < K:
        return 0
    visited = [False] * N
    return back_tracking(N, 0, K, A, GM, 0, [0, 0], visited, 0, 0, 0)


IN, IK = map(int, sys.stdin.readline().split())
IA = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
IGM = [list(map(lambda x:int(x) - 1, sys.stdin.readline().split())) for _ in range(2)]
print(solution(IN, IK, IA, IGM))
