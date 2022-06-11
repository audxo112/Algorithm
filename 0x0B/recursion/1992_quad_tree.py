# https://www.acmicpc.net/problem/1992
import sys


def split(N, sx, sy):
    yield sx, sy
    yield sx + N, sy
    yield sx, sy + N
    yield sx + N, sy + N


def recursion(N, board, sx, sy):
    if N == 1:
        return board[sy][sx]

    nn = N // 2
    tree = []
    il = 1
    for (x, y) in split(nn, sx, sy):
        item = recursion(nn, board, x, y)
        il *= len(item)
        tree.append(item)

    if il == 1 and tree[0] == tree[1] == tree[2] == tree[3]:
        return tree[0]
    return f"({''.join(tree)})"


def solution(N, board):
    return recursion(N, board, 0, 0)


IN = int(sys.stdin.readline())
IBoard = [sys.stdin.readline().rstrip() for _ in range(IN)]
print(solution(IN, IBoard))
