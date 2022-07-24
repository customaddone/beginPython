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
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

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

    # 0~p)まで求値
    def get(self, p):
        #assert 0 <= p < self.n
        p += self.size
        for i in range(1, self.log + 1):
            self.push(p >> i)
        return self.d[p]

    # [l, r)を求値
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

    # 区間に足し引きする
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
# 参考
# https://betrue12.hateblo.jp/entry/2020/09/23/005940

# (e1, e2): 今の所の総和, 何個足したか 遅延セグ木は個数をまとめることが必要

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


# 区間最小区間更新
# 使いやすいように

#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = 2**31 - 1
#################

class LazySegmentTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(l, r, x): 区間[l, r)をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        num: n以上の最小の2のべき乗
        data: 値配列(1-index)
        lazy: 遅延配列(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):
            """
            伝搬する対象の区間を求める
            lm: 伝搬する必要のある最大の左閉区間
            rm: 伝搬する必要のある最大の右開区間
            """
            l += self.num
            r += self.num
            lm = l >> (l & -l).bit_length()
            rm = r >> (r & -r).bit_length()

            while r > l:
                if l <= lm:
                    yield l
                if r <= rm:
                    yield r
                r >>= 1
                l >>= 1
            while l:
                yield l
                l >>= 1

    def propagates(self, *ids):
        """
        遅延伝搬処理
        ids: 伝搬する対象の区間
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v
            self.data[2 * i + 1] = v
            self.lazy[i] = None

    def update(self, l, r, x):
        """
        区間[l, r)の値をxに更新
        l, r: index(0-index)
        x: update value
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])


    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res

a = [1, 2, 3, 4, 5]
seg = LazySegmentTree(a, segfunc, ide_ele)
seg.update(0, 3, 2)
print(seg.query(0, 3))


# 区間最小区間加算

#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = 2**31 - 1
#################

class LazySegmentTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    add(l, r, x): 区間[l, r)にxを加算 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        num: n以上の最小の2のべき乗
        data: 値配列(1-index)
        lazy: 遅延配列(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):
            """
            伝搬する対象の区間を求める
            lm: 伝搬する必要のある最大の左閉区間
            rm: 伝搬する必要のある最大の右開区間
            """
            l += self.num
            r += self.num
            lm = l >> (l & -l).bit_length()
            rm = r >> (r & -r).bit_length()

            while r > l:
                if l <= lm:
                    yield l
                if r <= rm:
                    yield r
                r >>= 1
                l >>= 1
            while l:
                yield l
                l >>= 1

    def propagates(self, *ids):
        """
        遅延伝搬処理
        ids: 伝搬する対象の区間
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if not v:
                continue
            self.lazy[2 * i] += v
            self.lazy[2 * i + 1] += v
            self.data[2 * i] += v
            self.data[2 * i + 1] += v
            self.lazy[i] = 0

    def add(self, l, r, x):
        """
        区間[l, r)の値にxを加算
        l, r: index(0-index)
        x: additional value
        """
        *ids, = self.gindex(l, r)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] += x
                self.data[l] += x
                l += 1
            if r & 1:
                self.lazy[r - 1] += x
                self.data[r - 1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1]) + self.lazy[i]


    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res
