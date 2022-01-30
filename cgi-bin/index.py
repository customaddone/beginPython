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
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

def extGcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = extGcd(b % a, a)
    return g, x - (b // a) * y, y

# ax + by = cとなる(x, y)の一般項を求めてくれる
# (x, y) = (-b2 * t + x, -a2 * t + y) tは任意の整数
def form_ext(a1, b1, c):
    def extGcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = extGcd(b % a, a)
        return g, x - (b // a) * y, y
    g, x, y = extGcd(a1, b1)
    # 解なし
    if c % g != 0:
        return 0, []

    x *= c // g
    y *= c // g
    a2 = a1 // g
    b2 = b1 // g

    return 1, [-b2, x, a2, y]

print(form_ext(24, 49, 1))
