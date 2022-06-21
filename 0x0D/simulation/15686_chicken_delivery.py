# https://www.acmicpc.net/problem/15686
import sys


def back_tracking(N, M, dist, n, visited):
    if M == 0:
        DN = len(dist)
        return sum(min(map(lambda x: dist[i][x], visited)) for i in range(DN))

    val = float("inf")
    for i in range(n, N):
        visited.append(i)
        val = min(back_tracking(N, M - 1, dist, i + 1, visited), val)
        visited.pop()
    return val


def solution(N, M, board):
    c_pos = [(x, y) for y in range(N) for x in range(N) if board[y][x] == "2"]
    h_pos = [(x, y) for y in range(N) for x in range(N) if board[y][x] == "1"]
    dist = [[abs(cx - hx) + abs(cy - hy) for cx, cy in c_pos] for hx, hy in h_pos]
    return back_tracking(len(c_pos), M, dist, 0, [])


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [sys.stdin.readline().split() for _ in range(IN)]
print(solution(IN, IM, IBoard))
