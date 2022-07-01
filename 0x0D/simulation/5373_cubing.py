# https://www.acmicpc.net/problem/5373
import sys


def get(dr, r, cdr, cube):
    c_cube = cube[cdr]
    if dr == "L":
        if cdr == "D":
            if r == "+":
                return [c_cube[2][0], c_cube[1][0], c_cube[0][0]]
            return [c_cube[0][0], c_cube[1][0], c_cube[2][0]]
        elif cdr == "B":
            return [c_cube[2][2], c_cube[1][2], c_cube[0][2]]
        elif cdr == "U":
            if r == "+":
                return [c_cube[0][0], c_cube[1][0], c_cube[2][0]]
            return [c_cube[2][0], c_cube[1][0], c_cube[0][0]]
        elif cdr == "F":
            return [c_cube[0][0], c_cube[1][0], c_cube[2][0]]
    elif dr == "R":
        if cdr == "U":
            if r == "+":
                return [c_cube[2][2], c_cube[1][2], c_cube[0][2]]
            return [c_cube[0][2], c_cube[1][2], c_cube[2][2]]
        elif cdr == "B":
            return [c_cube[2][0], c_cube[1][0], c_cube[0][0]]
        elif cdr == "D":
            if r == "+":
                return [c_cube[0][2], c_cube[1][2], c_cube[2][2]]
            return [c_cube[2][2], c_cube[1][2], c_cube[0][2]]
        elif cdr == "F":
            return [c_cube[0][2], c_cube[1][2], c_cube[2][2]]
    elif dr == "U":
        if cdr == "F":
            if r == "+":
                return c_cube[0][::-1]
            return c_cube[0][:]
        elif cdr == "L":
            return [c_cube[2][0], c_cube[1][0], c_cube[0][0]]
        elif cdr == "B":
            if r == "+":
                return c_cube[0][:]
            return c_cube[0][::-1]
        elif cdr == "R":
            return [c_cube[0][2], c_cube[1][2], c_cube[2][2]]
    elif dr in "D":
        if cdr == "B":
            if r == "+":
                return c_cube[2][::-1]
            return c_cube[2][:]
        elif cdr == "L":
            return [c_cube[2][2], c_cube[1][2], c_cube[0][2]]
        elif cdr == "F":
            if r == "+":
                return c_cube[2][:]
            return c_cube[2][::-1]
        elif cdr == "R":
            return [c_cube[0][0], c_cube[1][0], c_cube[2][0]]
    elif dr == "F":
        if cdr == "L":
            if r == "+":
                return c_cube[0][::-1]
            return c_cube[0][:]
        elif cdr == "U":
            return c_cube[2][::-1]
        elif cdr == "R":
            if r == "+":
                return c_cube[0][:]
            return c_cube[0][::-1]
        elif cdr == "D":
            return c_cube[0][:]
    else:
        if cdr == "R":
            if r == "+":
                return c_cube[2][::-1]
            return c_cube[2][:]
        elif cdr == "U":
            return c_cube[0][::-1]
        elif cdr == "L":
            if r == "+":
                return c_cube[2][:]
            return c_cube[2][::-1]
        elif cdr == "D":
            return c_cube[2][:]


def put(dr, cdr, cube, data):
    c_cube = cube[cdr]
    if dr == "L":
        if cdr == "B":
            c_cube[0][2], c_cube[1][2], c_cube[2][2] = data
        else:
            c_cube[0][0], c_cube[1][0], c_cube[2][0] = data
    elif dr == "R":
        if cdr == "B":
            c_cube[0][0], c_cube[1][0], c_cube[2][0] = data
        else:
            c_cube[0][2], c_cube[1][2], c_cube[2][2] = data
    elif dr == "U":
        if cdr == "L":
            c_cube[0][0], c_cube[1][0], c_cube[2][0] = data
        elif cdr == "R":
            c_cube[0][2], c_cube[1][2], c_cube[2][2] = data
        else:
            c_cube[0] = data
    elif dr == "D":
        if cdr == "L":
            c_cube[0][2], c_cube[1][2], c_cube[2][2] = data
        elif cdr == "R":
            c_cube[0][0], c_cube[1][0], c_cube[2][0] = data
        else:
            c_cube[2] = data
    elif dr == "F":
        if cdr == "U":
            c_cube[2] = data
        else:
            c_cube[0] = data
    else:
        if cdr == "U":
            c_cube[0] = data
        else:
            c_cube[2] = data


def simulation(cube, move, dr, r):
    for _ in range(1 if r == "+" else 3):
        cube[dr] = list(map(list, zip(*cube[dr][::-1])))

    if r == "+":
        move = move[::-1]

    tmp = get(dr, r, move[0], cube)
    for i in range(3):
        put(dr, move[i], cube, get(dr, r, move[i + 1], cube))
    else:
        put(dr, move[3], cube, tmp)


def solution(N, rotate):
    move = {
        "L": "DBUF",
        "R": "UBDF",
        "U": "FLBR",
        "D": "BLFR",
        "F": "LURD",
        "B": "RULD",
    }
    cube = {
        "L": [['g'] * 3 for _ in range(3)],
        "R": [['b'] * 3 for _ in range(3)],
        "U": [['w'] * 3 for _ in range(3)],
        "D": [['y'] * 3 for _ in range(3)],
        "F": [['r'] * 3 for _ in range(3)],
        "B": [['o'] * 3 for _ in range(3)],
    }

    for i in range(N):
        dr, r = rotate[i]
        simulation(cube, move[dr], dr, r)

    return '\n'.join([''.join(line) for line in cube["U"]])


IT = int(sys.stdin.readline())
for _ in range(IT):
    IN = int(sys.stdin.readline())
    IRotate = sys.stdin.readline().split()
    print(solution(IN, IRotate))
