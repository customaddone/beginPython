# https://atcoder.jp/contests/abc106/tasks/abc106_b
# （条件)の個数を求めよ
# N <= 200なので全探索できる
import math
N = int(input())

# 約数の数を出してくれる
def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return len(divisors)

cnt = 0
# 1からNまでの奇数
for i in range(1, N + 1, 2):
    if make_divisors(i) == 8:
        cnt += 1
print(cnt)
