# https://www.acmicpc.net/problem/11559
import sys


def move(x, y):
    if x - 1 >= 0:
        yield x - 1, y
    if x + 1 < 6:
        yield x + 1, y
    if y - 1 >= 0:
        yield x, y - 1
    if y + 1 < 12:
        yield x, y + 1


def bfs(board, visited, sx, sy, turn):
    visited[sy][sx] = turn
    queue = [(sx, sy)]
    i, QN = 0, len(queue)
    while i < QN:
        x, y = queue[i]
        for nx, ny in move(x, y):
            if visited[ny][nx] == turn or board[ny][nx] != board[sy][sx]:
                continue
            visited[ny][nx] = turn
            queue.append((nx, ny))
        i, QN = i + 1, len(queue)
    if QN >= 4:
        for x, y in queue:
            board[y][x] = ""
        return True
    return False


def puyo(board):
    board = list(map(list, zip(*board)))
    for i, nb in enumerate(board):
        line = ''.join(nb)
        board[i] = "." * (12 - len(line)) + line
    return list(map(list, zip(*board)))


def solution(board):
    visited = [[0] * 6 for _ in range(12)]
    play, turn = True, 0
    while play:
        play, turn = False, turn + 1
        for y in range(11, -1, -1):
            empty = True
            for x in range(6):
                if board[y][x] != ".":
                    empty = False
                    if visited[y][x] < turn and bfs(board, visited, x, y, turn):
                        play = True
            if empty:
                break
        board = puyo(board)
    return turn - 1


IBoard = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
print(solution(IBoard))
