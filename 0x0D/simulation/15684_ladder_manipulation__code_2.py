# https://www.acmicpc.net/problem/15684
import sys


def simulation(N, H, board):
    for n in range(1, N - 1):
        c = n
        for h in range(1, H):
            if board[h][c]:
                c = board[h][c]
        if c != n:
            return False
    return True


def back_tracking(C, N, H, board, pos, l_cnt, ans):
    if C >= ans:
        return ans

    if simulation(N, H, board):
        return min(C, ans)
    elif C == 3:
        return ans

    odd = sum([cnt % 2 for cnt in l_cnt])
    if odd > 3 - C:
        return ans

    for x, y in pos:
        if board[y][x] or board[y][x + 1]:
            continue
        board[y][x], board[y][x + 1] = x + 1, x
        l_cnt[x] += 1
        ans = back_tracking(C + 1, N, H, board, pos, l_cnt, ans)
        board[y][x], board[y][x + 1] = 0, 0
        l_cnt[x] -= 1

    return ans


def solution(N, M, H, line):
    N, H = N + 1, H + 1
    board = [[0] * N for _ in range(H)]
    l_cnt = [0] * (N - 1)
    for y, x in line:
        board[y][x + 1], board[y][x] = x, x + 1
        l_cnt[x] += 1

    pos = [(x, y) for y in range(1, H) for x in range(1, N - 1) if board[y][x] == 0 and board[y][x + 1] == 0]
    answer = back_tracking(0, N, H, board, pos, l_cnt, 4)
    return answer if answer != 4 else -1


IN, IM, IH = map(int, sys.stdin.readline().split())
ILine = [tuple(map(int, sys.stdin.readline().split())) for _ in range(IM)]
print(solution(IN, IM, IH, ILine))
