# https://www.acmicpc.net/problem/14500
import sys


def move(N, M, x, y):
    if x - 1 >= 0:
        yield x - 1, y
    if x + 1 < M:
        yield x + 1, y
    if y - 1 >= 0:
        yield x, y - 1
    if y + 1 < N:
        yield x, y + 1


def back_tracking(N, M, C, board, visited, x, y, maxi, cur, ans):
    if C == 4:
        return max(cur, ans)

    if cur + (4 - C) * maxi <= ans:
        return ans

    maxVal = ans
    for nx, ny in move(N, M, x, y):
        if visited[ny][nx]:
            continue
        if C == 2:
            visited[ny][nx] = True
            maxVal = back_tracking(N, M, C + 1, board, visited, x, y, maxi, cur + board[ny][nx], maxVal)
            visited[ny][nx] = False

        visited[ny][nx] = True
        maxVal = back_tracking(N, M, C + 1, board, visited, nx, ny, maxi, cur + board[ny][nx], maxVal)
        visited[ny][nx] = False
    return maxVal


def solution(N, M, board):
    visited = [[False] * M for _ in range(N)]
    maxi = max(map(max, board))
    maxVal = 0
    for (x, y) in [(x, y) for y in range(N) for x in range(M)]:
        visited[y][x] = True
        maxVal = back_tracking(N, M, 0, board, visited, x, y, maxi, 0, maxVal)
        if maxVal == maxi * 4:
            return maxVal
        visited[y][x] = False
    return maxVal


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IM, IBoard))
