
# sum 의 기본 값은 0 이므로 [1,2,3] -> 0 + 1 + 2 + 3 이 되는데
# 2차원 배열의 경우 기본 값을 [] 초기화 해서 1차원 배여로 변경
# 다시 한번 sum 을 사용 하여 2차원 배열의 합을 구한다
# sum 은 for 를 이용해 더하는 것보다 5배정도 빠르다
def arr2d_count(arr):
    return sum(sum(sum(arr, [])))


# 2차원 배열 에서 각각 자식을 tuple 로 바꿔야 할때
# 속도는 두개 다 비슷
def list_to_tuple1(arr):
    return list(zip(*list(zip(*arr))))


def list_to_tuple2(arr):
    return list(map(tuple, arr))


# 0,0 -> n, n 기준 으로 뒤집을 때
# 1 2 3     1 4 7
# 4 5 6 ->  2 5 8
# 7 8 9     3 6 9
def list_flip(arr):
    return list(zip(*arr))


def list_flip_2(arr):
    return list(map(list, zip(*arr)))


# 리스트 90도 회전
# 1 2 3     7 4 1
# 4 5 6 ->  8 5 2
# 7 8 9     9 6 3
def list_rotate90(arr):
    return list(zip(*arr[::-1]))


# 4분할을 할때 유용함
#  1  2  3  4
#  5  6  7  8  ->    [ 1  2 ] [ 3  4 ] [  9 10 ] [ 11 12 ]
#  9 10 11 12  ->    [ 5  6 ] [ 7  8 ] [ 13 14 ] [ 15 16 ]
# 13 14 15 16

def arr2d_divide(arr):
    n = len(arr)
    m = n // 2
    if m == 0:
        return
    for i in range(0, n, m):
        for j in range(0, n, m):
            arr2d_divide([ar[j:j + m] for ar in arr[i:i + m]])


#  행렬 누산 O(M*N)
#  N  0  0 -N   ->  N  N  N  0
#
#  N  0  0 -N       N  N  N  0
#  0  M -M  0   ->  N NM  N  0
# -N -M  M  N   ->  0  0  0  0
#  0  0  0  0       0  0  0  0
def acc_array():
    n = 3
    cal = [
        (0, 0, 2, 2, 3),
        (1, 0, 2, 2, -1),
        (0, 0, 2, 1, 2),
    ]
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for (sx, sy, ex, ey, amt) in cal:
        arr[sy][sx] += amt
        arr[ey + 1][sx] -= amt
        arr[sy][ex + 1] -= amt
        arr[ey + 1][ex + 1] += amt

    for i in range(n):
        for j in range(1, n):
            arr[i][j] += arr[i][j - 1]

    for j in range(n):
        for i in range(1, n):
            arr[i][j] += arr[i - 1][j]

    for ar in arr:
        print(ar)


if __name__ == "__main__":
    acc_array()