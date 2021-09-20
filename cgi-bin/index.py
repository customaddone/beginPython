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

"""
O(N^{0.75}) solution
"""


from functools import lru_cache

@lru_cache(None)
def f(L, R):
    """
    L < x, y <= R であって、gcd(x,y) == 1 となるものを数える。
    """

    res = (R - L)**2
    """
    ここから、 d = gcd(x,y) >= 2 となるものを引いていく。
    これは、 l = L // d, r = R // d として、f(L//d, R//d) 通りである。
    (l, r) が O(sqrt(L+R)) 通りしかないことから、f(L, R) はより小さな場合の
    f(l, r) を O(sqrt(L+R)) 件使って計算できる。
    """
    def find_nxt_d(d):
        """
        いまの (l, r) = (L//d, R//d) よりも大きな (l, r) が出てくる次の d を求める
        """
        d1 = L // (L // d + 1)
        d2 = R // (R // d + 1)
        return max(d1, d2)

    d = max(L, R)
    while d > 1:
        nxt_d = find_nxt_d(d)
        res -= (d - nxt_d) * f(L // d, R // d)
        d = nxt_d
    return res

def g(L, R):
    """
    L < x, y <= R であって、x | y となるものを数える。
    x = d ごとに数える。
    これは、 l = L // d, r = R // d として、r - l 通りであるから、f と同様に計算できる。
    """
    def find_nxt_d(d):
        """
        いまの (l, r) = (L//d, R//d) よりも大きな (l, r) が出てくる次の d を求める
        """
        d1 = L // (L // d + 1)
        d2 = R // (R // d + 1)
        return max(d1, d2)

    res = 0
    d = max(L, R)
    while d:
        nxt_d = find_nxt_d(d)
        # (nxt_d, d] の中で (L, R] との交わりの大きさ
        cnt = max(0, min(d, R) - max(nxt_d, L))
        res += cnt * (R // d - L // d)
        d = nxt_d
    return res

def main(L, R):
    """
    半開区間　(L, R] として持つ。
    dx in (L, R] iff x in (L//d, R//d] と簡潔に書ける利点がある。
    """
    L -= 1
    """
    g == 1, g == x, g == y という 3 条件で包除
    """
    ___ = (R - L)**2
    o__ = f(L, R)
    _o_ = g(L, R)
    __o = g(L, R)
    oo_ = R - L if L < 1 <= R else 0
    o_o = R - L if L < 1 <= R else 0
    _oo = R - L
    ooo = 1 if L < 1 <= R else 0
    return ___ - o__ - _o_ - __o + oo_ + o_o + _oo - ooo

# main(3, 7), main(4,10), main(1, 10**6)

L, R = map(int, input().split())
print(main(L, R))
