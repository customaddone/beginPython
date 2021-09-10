from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# k回回しても同じになるネックレスの集め方
# 最大のネックレスを作ろう
# abcabcabcなら3-beautifull, 6-beau, 9-beau...
# 同じm個の塊をt個並べるとn * m beauになる
# つまりk-beauにするにはkの約数i個の塊をいくつか作ればいい
# [1, 1, 5, 6, 7]
# a * 3, b * 6, c * 6
# aaabb は5個の塊

T = getN()
for _ in range(T):
    N, M = getNM()
    S = input()
    d = defaultdict(int)
    for s in S:
        d[s] += 1
    d = sorted(d.values())
    now, ans = float('inf'), 0
    divisors = make_divisors(M)

    # t-time repeat
    for t in range(1, max(d) + 1):
        # the max m-size of blocks
        opt = sum([d[i] // t for i in range(len(d))])
        # make div-size blocks
        for div in divisors:
            if opt >= div:
                ans = max(ans, div * t)
    print(ans)
