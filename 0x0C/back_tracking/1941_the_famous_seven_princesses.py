# https://www.acmicpc.net/problem/1941
import sys


def move(x, y):
    dirs = []
    if x + 1 < 5:
        dirs.append((x + 1, y))
    if x - 1 >= 0:
        dirs.append((x - 1, y))
    if y + 1 < 5:
        dirs.append((x, y + 1))
    if y - 1 >= 0:
        dirs.append((x, y - 1))
    return dirs


def back_tracking(board, visited, route, S, path, found):
    if 7 - len(path) + S < 4:
        return

    if len(path) == 7:
        if S >= 4:
            ans = tuple(sorted(path))
            if ans not in found:
                found.add(ans)
        return

    for i, (x, y) in enumerate(route):
        if visited[y][x]:
            continue

        visited[y][x] = True
        path.append(y * 5 + x)
        back_tracking(board, visited, route[i + 1:] + move(x, y), S + (board[y][x] == "S"), path, found)
        visited[y][x] = False
        path.pop()


def solution(board):
    visited = [[False] * 5 for _ in range(5)]
    pos = [(x, y) for y in range(5) for x in range(5)]

    cnt = 0
    for (x, y) in pos[:-6]:
        found = set()
        back_tracking(board, visited, [(x, y)], 0, [], found)
        cnt += len(found)
        visited[y][x] = True
    return cnt


IBoard = [sys.stdin.readline().rstrip() for _ in range(5)]
print(solution(IBoard))
