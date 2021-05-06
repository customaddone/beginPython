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
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353

INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############
# ACL
class LazySegmentTree():
    def __init__(self, n, op, e, mapping, composition, id):
        self.n = n
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e] * (2 * self.size)
        self.lz = [id] * (self.size)

    def update(self, k):
#        print(self.d)
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        self.all_apply(2 * k, self.lz[k])
        self.all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.id

    def build(self, arr):
        #assert len(arr) == self.n
        for i, a in enumerate(arr):
            self.d[self.size + i] = a
        for i in range(1, self.size)[::-1]:
            self.update(i)

    def set(self, p, x):
        #assert 0 <= p < self.n
        p += self.size
        for i in range(1, self.log + 1)[::-1]:
            self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        #assert 0 <= p < self.n
        p += self.size
        for i in range(1, self.log + 1):
            self.push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        #assert 0 <= l <= r <= self.n
        if l == r: return self.e
        l += self.size
        r += self.size
        for i in range(1, self.log + 1)[::-1]:
            if ((l >> i) << i) != l: self.push(l >> i)
            if ((r >> i) << i) != r: self.push(r >> i)
        sml = smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def apply(self, p, f):
        #assert 0 <= p < self.n
        p += self.size
        for i in range(1, self.log + 1)[::-1]:
            self.push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def range_apply(self, l, r, f):
        #assert 0 <= l <= r <= self.n
        if l == r: return
        l += self.size
        r += self.size
        for i in range(1, self.log + 1)[::-1]:
            if ((l >> i) << i) != l: self.push(l >> i)
            if ((r >> i) << i) != r: self.push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l: self.update(l >> i)
            if ((r >> i) << i) != r: self.update((r - 1) >> i)

    def max_right(self, l, g):
        #assert 0 <= l <= self.n
        #assert g(self.e)
        if l == self.n: return self.n
        l += self.size
        for i in range(1, self.log + 1)[::-1]:
            self.push(l >> i)
        sm = self.e
        while True:
            while l % 2 == 0: l >>= 1
            if not g(self.op(sm, self.d[l])):
                while l < self.size:
                    self.push(l)
                    l = 2 * l
                    if g(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l: return self.n

    def min_left(self, r, g):
        #assert 0 <= r <= self.n
        #assert g(self.e)
        if r == 0: return 0
        r += self.size
        for i in range(1, self.log + 1)[::-1]:
            self.push((r - 1) >> i)
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1
            if not g(self.op(self.d[r], sm)):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r: return 0

mod = 998244353
N, Q = getNM()
O = [1] * (N + 1) # 1, 11, 111, 1111...のmod
P = [1] * (N + 1) # 10^Nをmodしたもの
c = kk = 1
for i in range(1, N + 1):
    O[i] = c
    kk = kk * 10 % mod
    P[i] = kk
    c = (c + kk) % mod

# LST = LazySegmentTree(N, op, e, mapping, composition, id)
# op: 区間取得演算
# e: opの単位元
# mapping: 遅延評価演算
# composition: 各mapping間の遅延評価の関係 つまりmapとmapを合成して一つにする
# id: mappingの単位元

# 区間最小区間加算の場合は
# op: min(x, y)
# e: float('inf')
# mapping x + f
# composition: f + g
# id: 0
# ぐらいになる

# これは普通のセグ木と同様
def op(x, y):
    # (yの桁数分だけx[0]をシフトした分 + y[0]のmod, 新しくできた数字の桁数)を返す
    return ((P[y[1]] * x[0] + y[0]) % mod, x[1] + y[1])

# ここから遅延評価の関数
def mapping(p, x):
    # p: 書き換えが行われるなら1 ~ 9　なければ1
    # 桁数分だけ数字を書き換える
    # p = 7, x[0] = 1122 なら 7777 を返す
    if p:
        return (O[x[1]] * p % mod, x[1])
    return x

# 新しい操作pと前の操作qとの関係
def composition(p, q):
    # 書き換えが行われるなら上書き
    if p == 0: return q
    return p

res = [(1, 1)] * N
LST = LazySegmentTree(N, op, (0, 0), mapping, composition, 0)
LST.build(res)
for _ in range(Q):
    l, r, D = getNM()
    LST.range_apply(l - 1, r , D)
    print(LST.all_prod()[0])
