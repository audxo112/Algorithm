# https://www.acmicpc.net/problem/14889
import sys


def score(board, team, n):
    return sum([board[t][n] + board[n][t] for t in team])


def back_tracking(N, M, board, n, a_team, b_team, a_val, b_val, m_val):
    b_team = b_team[:]
    if M == 0:
        for i in range(n, N):
            b_team.append(i)
            b_val += score(board, b_team, i)
        print(a_team, b_team, a_val,b_val)
        return min(abs(a_val - b_val), m_val)

    for i in range(n, N):
        a_team.append(i)
        m_val = back_tracking(N, M - 1, board, i + 1, a_team, b_team, a_val + score(board, a_team, i), b_val, m_val)
        if m_val == 0:
            return 0
        a_team.pop()
        b_team.append(i)
        b_val += score(board, b_team, i)

    return m_val


def solution(N, board):
    return back_tracking(N, N // 2, board, 0, [], [], 0, 0, 1000000000)


IN = int(sys.stdin.readline())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IBoard))
