# https://www.acmicpc.net/problem/16235
# 한번에 처리 할 수 있으면 한번에 처리 하도록 변경
import sys


dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def solution(N, M, K, A, info):
    foods = [[5] * N for _ in range(N)]
    trees = [[{} for _ in range(N)] for _ in range(N)]

    for y, x, age in info:
        trees[y - 1][x - 1][age] = 1

    for k in range(K):
        breading = dict()
        for y in range(N):
            for x in range(N):
                if not trees[y][x]:
                    foods[y][x] += A[y][x]
                    continue
                bread = death = 0
                exist = True
                nxt = dict()
                for age, count in sorted(trees[y][x].items()):
                    if exist:
                        num = foods[y][x] // age
                        if num >= count:
                            foods[y][x] -= age * count
                            nxt[age + 1] = count
                            if not (age + 1) % 5:
                                bread += count
                        else:
                            if num:
                                foods[y][x] -= age * num
                                nxt[age + 1] = num
                                if not (age + 1) % 5:
                                    bread += num
                            exist = False
                            death += (age >> 1) * (count - num)
                    else:
                        death += (age >> 1) * count
                trees[y][x] = nxt
                foods[y][x] += death + A[y][x]
                if bread:
                    for (dx, dy) in dirs:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if (nx, ny) not in breading:
                            breading[(nx, ny)] = bread
                        else:
                            breading[(nx, ny)] += bread

        for (x, y), cnt in breading.items():
            trees[y][x][1] = cnt

    return sum([sum(trees[y][x].values()) for x in range(N) for y in range(N)])


IN, IM, IK = map(int, sys.stdin.readline().split())
IA = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
IInfo = [list(map(int, sys.stdin.readline().split())) for _ in range(IM)]
print(solution(IN, IM, IK, IA, IInfo))
