# https://www.acmicpc.net/problem/1780
import sys


def recursion(N, board, answer):
    if N == 1:
        answer[board[0][0] + 1] += 1
        return

    if board[0][0] == 0:
        for i in range(N):
            if board[i].count(0) != N:
                break
        else:
            answer[1] += 1
            return
    else:
        ns = sum(map(sum, board)) // (N * N)
        if ns != 0:
            answer[ns + 1] += 1
            return

    nn = N // 3
    for y in range(0, N, nn):
        for x in range(0, N, nn):
            recursion(nn, [board[ny][x:x + nn] for ny in range(y, y + nn)], answer)


def solution(N, board):
    answer = [0, 0, 0]
    recursion(N, board, answer)
    return answer


IN = int(sys.stdin.readline())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
OAnswer = solution(IN, IBoard)
for OAns in OAnswer:
    print(OAns)
