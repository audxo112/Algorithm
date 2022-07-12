# https://www.acmicpc.net/problem/17837
import sys


dirs = [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]
cd = [0, 2, 1, 4, 3]


def simulation(board, piece, place, num, blue):
    y, x, d = piece[num]
    dx, dy = dirs[d]
    nx, ny = x + dx, y + dy

    if board[ny][nx] == 2:
        if blue:
            return False
        else:
            piece[num][2] = cd[d]
            return simulation(board, piece, place, num, True)
    else:
        cur = place[y][x]
        idx = cur.index(num)
        place[y][x], move = cur[:idx], cur[idx:]
        for i in move:
            piece[i][:2] = [ny, nx]
        if board[ny][nx] == 0:
            place[ny][nx] += move
        else:
            place[ny][nx] += move[::-1]
    return len(place[ny][nx]) >= 4


def solution(N, K, board, piece):
    for y in range(N):
        board[y] = [2] + board[y] + [2]
    board = [[2] * (N + 2)] + board + [[2] * (N + 2)]

    place = [[[] for _ in range(N + 2)] for _ in range(N + 2)]
    for i, (y, x, d) in enumerate(piece):
        place[y][x].append(i)

    for turn in range(1, 1001):
        for num in range(K):
            if simulation(board, piece, place, num, False):
                return turn
    return -1


IN, IK = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
IPiece = [list(map(int, sys.stdin.readline().split())) for _ in range(IK)]
print(solution(IN, IK, IBoard, IPiece))
