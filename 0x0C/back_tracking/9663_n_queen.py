# https://www.acmicpc.net/problem/9663
import sys


def back_tracking(N, row, queen, m_slope, p_slope):
    if row == N:
        return 1

    cnt = 0
    for col in range(N if row else N // 2):
        if not queen[col] and not m_slope[row - col] and not p_slope[row + col]:
            queen[col] = m_slope[row - col] = p_slope[row + col] = True
            cnt += back_tracking(N, row + 1, queen, m_slope, p_slope)
            queen[col] = m_slope[row - col] = p_slope[row + col] = False
    return cnt


def solution(N):
    queen = [False] * N
    m_slope = [False] * (2 * N - 1)
    p_slope = [False] * (2 * N - 1)
    if N % 2 == 0:
        return back_tracking(N, 0, queen, m_slope, p_slope) * 2
    else:
        answer = back_tracking(N, 0, queen, m_slope, p_slope) * 2
        col = N // 2
        queen[col] = m_slope[-col] = p_slope[col] = True
        return answer + back_tracking(N, 1, queen, m_slope, p_slope)


IN = int(sys.stdin.readline())
print(solution(IN))
