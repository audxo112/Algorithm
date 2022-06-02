# https://www.acmicpc.net/problem/16920
import sys
from collections import deque, defaultdict


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(N, M, P, turn, board):
    zero = 0
    area = [0] * (P + 1)
    queues = defaultdict(lambda: deque())
    for y in range(N):
        for x, c in enumerate(board[y]):
            if c == ".":
                zero += 1
            if c.isdigit():
                p = int(c)
                area[p] += 1
                board[y][x] = p
                queues[p].append((x, y))

    players = list(range(1, P + 1))
    while players:
        for p in players[:]:
            for _ in range(turn[p - 1]):
                queue = queues[p]
                if not queue:
                    players.remove(p)
                    break

                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for (dx, dy) in dirs:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ny][nx] != ".":
                            continue
                        board[ny][nx] = p
                        queue.append((nx, ny))
                        area[p] += 1
                        zero -= 1
                        if zero == 0:
                            return ' '.join(map(str, area[1:]))
    return ' '.join(map(str, area[1:]))


IN, IM, IP = map(int, sys.stdin.readline().split())
ITurn = list(map(int, sys.stdin.readline().split()))
IBoard = [list(sys.stdin.readline().rstrip()) for _ in range(IN)]
print(solution(IN, IM, IP, ITurn, IBoard))
