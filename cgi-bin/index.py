def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N = 24
if N == 1:
    print(0)
    exit()

# 1(1), 2(1 + 2), 3(1 + 2 + 3)...を超えられるか
def factime(ny):
    cnt = 1
    sum = 0
    while True:
        if sum + cnt > ny:
            return cnt - 1
            break
        sum += cnt
        cnt += 1
# 1
print(factime(2))
# 2
print(factime(3))
# 3
print(factime(9))
# 4 (1 + 2 + 3 + 4)
print(factime(10))
# 素因数分解
def prime_factorize(n):
    divisors = []
    # 27(2 * 2 * 7)の7を出すためにtemp使う
    temp = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                # 素因数を見つけるたびにtempを割っていく
                temp //= i
            divisors.append([i, cnt])
    if temp != 1:
        divisors.append([temp, 1])
    if divisors == []:
        divisors.append([n, 1])

    return divisors

ans = 0
for i in prime_factorize(N):
    ans += factime(i[1])
# 3
print(ans)
