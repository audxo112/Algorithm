# https://www.acmicpc.net/problem/15684
import sys


def simulation(N, H, board):
    for n in range(1, N - 1):
        c = n
        for h in range(1, H):
            c += board[h][c]
        if c != n:
            return False
    return True


def back_tracking(C, N, H, n, board, pos, l_cnt, ans):
    if C >= ans:
        return ans
    elif simulation(N, H, board):
        return min(C, ans)

    if C == 3:
        return ans

    odd = sum([cnt % 2 for cnt in l_cnt])
    if odd > 3 - C:
        return ans

    for i in range(n, len(pos)):
        x, y = pos[i]
        if board[y][x] or board[y][x + 1]:
            continue
        board[y][x], board[y][x + 1] = 1, -1
        l_cnt[x] += 1
        ans = back_tracking(C + 1, N, H, i + 1, board, pos, l_cnt, ans)
        board[y][x] = board[y][x + 1] = 0
        l_cnt[x] -= 1

    return ans


def solution(N, M, H, line):
    N, H = N + 1, H + 1
    board = [[False] * N for _ in range(H)]
    l_cnt = [0] * (N - 1)
    for y, x in line:
        board[y][x], board[y][x + 1] = 1, -1
        l_cnt[x] += 1

    pos = [(x, y) for y in range(1, H) for x in range(1, N - 1) if not board[y][x] and not board[y][x + 1]]
    answer = back_tracking(0, N, H, 0, board, pos, l_cnt, 4)
    return answer if answer != 4 else -1


IN, IM, IH = map(int, sys.stdin.readline().split())
ILine = [tuple(map(int, sys.stdin.readline().split())) for _ in range(IM)]
print(solution(IN, IM, IH, ILine))
