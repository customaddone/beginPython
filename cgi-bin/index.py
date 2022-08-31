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
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# sys.setrecursionlimit(10000000)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
inf = float('inf')
eps = 10 ** (-12)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

class Multiset():
    # 数字の最大サイズのbit長を入れる
    def __init__(self, digit):
        self.d = defaultdict(int)
        self.digit = digit
        self.size = 0

    def add(self, a, i):
        c = 0
        self.size += i
        for k in range(self.digit - 1, -2, -1):
            self.d[(c, k + 1)] += i
            if k >= 0:
                c += (a & (1 << k))

    def size_all(self):
        return self.size

    # xが何個あるか
    def find(self, x):
        return self.d[(x, 0)]

    # set中にpi^x < tarなるpiがいくつ含まれるか
    def xor_count(self, x, tar):
        c, res = 0, 0
        for k in range(self.digit - 1, -1, -1):
            # tarのフラグが1の時のみカウントが進む
            res += self.d[(c ^ (x & (1 << k)), k)] * (((tar & (1 << k)) > 0))
            c += ((tar ^ x) & (1 << k))
        return res

    # pi^xをソートするとlim個目のpi^xは何になるか　^xして元に戻す
    def xor_bound(self, x, lim):
        c, tar, res = 0, 0, 0
        for k in range(self.digit - 1, -1, -1):
            # フラグを立てるとself.d[(c ^ (x & (1 << k)), k)]だけカウントが進む
            # resが許容内ならtarにフラグを立てる
            if res + self.d[(c ^ (x & (1 << k)), k)] < lim:
                tar += (1 << k)
                res += self.d[(c ^ (x & (1 << k)), k)]
            c += ((tar ^ x) & (1 << k))
        return tar

V = Multiset(32)
N = getN()
for _ in range(N):
    q = getList()
    if q[0] == 1:
        V.add(q[1], 1)
    elif q[0] == 2:
        V.add(q[1], -1)
    else:
        print(V.xor_count(q[1], q[2]))
