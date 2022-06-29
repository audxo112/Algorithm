from math import gcd


# for - else 구문, while - else 도 같음
def for_else():
    for i in range(5):
        if i == 3:
            break
    else:
        print("break 로 빠져 나오지 않은 정상 loop 종료시 실행")


# 최대 공약수
def num_gcd(x, y):
    return gcd(x, y)


# 최소 공배수
def num_lcm(x, y):
    return x * y // gcd(x, y)
