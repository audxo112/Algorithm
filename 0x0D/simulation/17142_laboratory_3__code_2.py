# https://www.acmicpc.net/problem/17142
import sys
from collections import deque


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def back_tracking(N, M, n=0, selected=[]):
    m = len(selected)
    if M == m:
        return [selected[:]]
    arr = []
    for i in range(n, N):
        if N - i < M - m:
            continue
        selected.append(i)
        arr += back_tracking(N, M, i + 1, selected)
        selected.pop()
    return arr


def bfs(N, board, visited, x, y, idx):
    queue = deque([(x, y)])
    time = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx] == 1 or visited[(nx, ny)][idx] != 9999:
                    continue
                visited[(nx, ny)][idx] = time
                queue.append((nx, ny))
        time += 1


def simulation(virus, pos_logs, best):
    max_val = 0
    for log in pos_logs:
        min_val = 9999
        for i in virus:
            if log[i] < min_val:
                min_val = log[i]
        if min_val >= best:
            return best
        elif min_val > max_val:
            max_val = min_val
    return max_val


def solution(N, M, board):
    visited = {}
    pos = [(x, y) for x in range(N) for y in range(N) if board[y][x] == 2]
    PN = len(pos)
    for y in range(N):
        for x in range(N):
            if board[y][x] == 2:
                visited[(x, y)] = [9999] * PN
            elif not board[y][x]:
                visited[(x, y)] = [9999] * PN
    zero = N * N - sum(sum(board, [])) + PN
    if zero == 0:
        return 0

    for i, (x, y) in enumerate(pos):
        bfs(N, board, visited, x, y, i)
    for x, y in pos:
        visited[(x, y)] = [0] * PN

    pos_logs = list(visited.values())
    answer = 9999
    for virus in back_tracking(PN, M):
        answer = simulation(virus, pos_logs, answer)

    return answer if answer != 9999 else -1


IN, IM = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
print(solution(IN, IM, IBoard))
