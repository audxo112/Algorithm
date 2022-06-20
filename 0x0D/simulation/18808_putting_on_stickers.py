# https://www.acmicpc.net/problem/18808
import sys


def rotate(sticker):
    for _ in range(4):
        yield sticker
        sticker = list(zip(*sticker[::-1]))


def attach(board, sticker, sx, sy):
    SN, SM = len(sticker), len(sticker[0])
    pos = [(x, y) for y in range(SN) for x in range(SM) if sticker[y][x] == 1]
    for x, y in pos:
        if board[y + sy][x + sx] == 1:
            return False
    for x, y in pos:
        board[y + sy][x + sx] = 1
    return True


def putting(N, M, board, sticker):
    SN, SM = len(sticker), len(sticker[0])
    for y in range(N - SN + 1):
        for x in range(M - SM + 1):
            if attach(board, sticker, x, y):
                return True
    return False


def solution(N, M, stickers):
    board = [[0] * M for _ in range(N)]

    for stk in stickers:
        for sticker in rotate(stk):
            if putting(N, M, board, sticker):
                break
    return sum(sum(board, []))


IN, IM, IK = map(int, sys.stdin.readline().split())
IStickers = []
for _ in range(IK):
    ISN, ISM = map(int, sys.stdin.readline().split())
    ISticker = [list(map(int, sys.stdin.readline().split())) for _ in range(ISN)]
    IStickers.append(ISticker)
print(solution(IN, IM, IStickers))
