from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# 約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# [1, 2, 3, 4, 6, 12]
print(make_divisors(12))

# 公約数列挙
def make_divisors(m, n):
    divisors = []
    numi = min(m, n)
    numa = max(m, n)
    for i in range(1, int(math.sqrt(numi)) + 1):
        if numi % i == 0:
            if numa % i == 0:
                divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != numi // i and numa % (numi // i) == 0:
                divisors.append(numi // i)
    return sorted(divisors)
# [1, 2, 3, 6]
print(make_divisors(12, 18))

# ユークリッド互除法
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)
# 6
print(euclid(12, 18))

# 最小公倍数
def lcm(x, y):
    return x * (y // math.gcd(x, y))

# 36
print(lcm(12, 18))
