# https://www.acmicpc.net/problem/14500
import sys


def init_blocks():
    base = [
        [[1, 1, 1, 1]],
        [[1, 1], [1, 1]],
        [[1, 0], [1, 0], [1, 1]],
        [[1, 0], [1, 1], [0, 1]],
        [[1, 1, 1], [0, 1, 0]]
    ]
    blocks = []
    for block in base:
        for fi in range(2):
            if fi != 0:
                block = list(map(list, zip(*block)))
            for ri in range(4):
                if ri != 0:
                    block = list(map(list, zip(*block[::-1])))
                if block not in blocks:
                    blocks.append(block)
    return blocks


def simulation(N, M, board, block):
    BN, BM = len(block), len(block[0])
    maxVal = 0
    for y in range(N - BN + 1):
        for x in range(M - BM + 1):
            total = 0
            for by in range(BN):
                for bx in range(BM):
                    total += board[y + by][x + bx] * block[by][bx]
            maxVal = max(total, maxVal)
    return maxVal


def solution(N, M, board):
    blocks = init_blocks()
    maxVal = 0
    for block in blocks:
        maxVal = max(simulation(N, M, board, block), maxVal)
    return maxVal


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IM, IBoard))
