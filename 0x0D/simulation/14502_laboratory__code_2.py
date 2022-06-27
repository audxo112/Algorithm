# https://www.acmicpc.net/problem/14502
import sys


dirs8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (1, 1), (0, 1), (-1, 1)]


def bfs(board, plague, visited, zero):
    queue = [] + plague
    for x, y in queue:
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if board[ny][nx] or visited[ny][nx]:
                continue
            zero -= 1
            visited[ny][nx] = True
            queue.append((nx, ny))
    return zero


def exist_wall(board, x, y):
    for dx, dy in dirs8:
        if board[y + dy][x + dx] == 1:
            return True
    return False


def make_candi(board, pos, x, y):
    return [(x + dx, y + dy) for dx, dy in dirs8 if board[y + dy][x + dx] == 0 and (x + dx, y + dy) not in pos]


def back_tracking(C, n, board, plague, visited, zero, pos, ans):
    if C == 3:
        return max(bfs(board, plague, [v[:] for v in visited], zero), ans)

    for i in range(n, len(pos)):
        x, y = pos[i]
        n_pos = pos + make_candi(board, pos, x, y)
        board[y][x] = 1
        ans = back_tracking(C + 1, i + 1, board, plague, visited, zero, n_pos, ans)
        board[y][x] = 0

    return ans


def solution(N, M, board):
    board = [[1] * (M + 2)] + board
    for y in range(1, N + 1):
        board[y] = [1] + board[y] + [1]
    board = board + [[1] * (M + 2)]
    N, M = N + 2, M + 2

    plague, pos = [], []
    zero = -3
    for y in range(1, N - 1):
        zero += board[y].count(0)
        for x in range(1, M - 1):
            if board[y][x] == 2:
                plague.append((x, y))
            elif board[y][x] == 0 and exist_wall(board, x, y):
                pos.append((x, y))

    visited = [[False] * M for _ in range(N)]
    for px, py in plague:
        visited[py][px] = True

    return back_tracking(0, 0, board, plague, visited, zero, pos, 0)


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IM, IBoard))
