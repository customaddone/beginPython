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

from functools import lru_cache

@lru_cache(None)
def f(A, B):
    """
    A < x, y <= B であって、gcd(x,y) == 1 となるものを数える。
    """

    res = (B - A)**2
    """
    ここから、 d = gcd(x,y) >= 2 となるものを引いていく。
    これは、 a = A // d, b = B // d として、f(a, b) 通りである。
    (a, b) が O(sqrt(B)) 通りしかないことから、f(A, B) はより小さな場合の
    f(a, b) を O(sqrt(B)) 件使って計算できる。
    """
    R = B
    while R > 1:
        a, b = A // R, B // R
        L = max(A // (a + 1), B // (b + 1))
        res -= (R - L) * f(a, b)
        R = L
    return res

def g(A, B):
    """
    A < x, y <= B であって、x | y となるものを数える。
    x = d ごとに数える。
    これは、 a = A // d, b = B // d として、b - a 通りであるから、f と同様に計算できる。
    """
    res = 0
    R = B
    while R:
        a, b = A // R, B // R
        L = max(A // (a + 1), B // (b + 1))
        cnt = max(0, min(R, B) - max(L, A))
        res += cnt * (b - a)
        R = L
    return res

def main(A, B):
    """
    半開区間　(A, B] として持つ。
    """
    A -= 1
    """
    g == 1, g == x, g == y という 3 条件で包除
    """
    ___ = (B - A)**2
    o__ = f(A, B)
    _o_ = g(A, B)
    __o = g(A, B)
    oo_ = B - A if A == 0 else 0
    o_o = B - A if A == 0 else 0
    _oo = B - A
    ooo = 1 if A == 0 else 0
    return ___ - o__ - _o_ - __o + oo_ + o_o + _oo - ooo

# main(3, 7), main(4,10), main(1, 10**6)

A, B = map(int, input().split())
print(main(A, B))
