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

#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = float('inf')
#################

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    def add(self, a, w):
        x = a
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

    def lowerbound(self,w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x + 1

N = 10
A = [0] + [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] # 1-indexに
Q = 10
query = [
[1, 1, 2],
[2, 2, 5],
[1, 1, 1],
[1, 3, 8],
[2, 6, 9],
[2, 5, 8],
[1, 8, 3],
[2, 1, 2],
[2, 5, 10],
[2, 3, 7],
]

event = [[] for i in range(9 + 1)] # 実際には圧縮する
seg = SegTree([float('inf')] * (N + 1), segfunc, ide_ele)

# 計算量O(N）
for i in range(1, N + 1):
    event[A[i]].append([1, -1, i, 1]) # Aの書き込み
    seg.update(i, A[i])

# 計算量O(QlogQ)
for i in range(Q):
    kind, in1, in2 = query[i]
    # フラグ書き込み、消去
    if kind == 1:
        prev = A[in1]
        event[in2].append([1, i, in1, 1]) # 書き込み
        event[prev].append([1, i, in1, -1]) # 消去
        A[in1] = in2
        seg.update(in1, in2)
    # クエリ
    else:
        target = seg.query(in1, in2) # [l, r)の最小値を求める
        event[target].append([2, i, in1, 0])

# 計算量O(log(N + Q) * (N + Q))
# イベントのソートがネックになる
ans = []
for i in range(1, 9 + 1):
    bit = BIT(N)
    event[i].sort(key = lambda j: j[1])
    for kind, que, place, a in event[i]:
        # 書き込み
        if kind == 1:
            bit.add(place, a)
        else:
            # pleceより右に立っているフラグの中で一番左にあるもの
            c = bit.get(place)
            ans.append([que, bit.lowerbound(c + 1)])

ans.sort()
print(ans) # [[1, 2], [4, 7], [5, 7], [7, 1], [8, 7], [9, 4]]
