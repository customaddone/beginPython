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

# ここの設定を変えて使う
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

N, M = getNM()
seg = SegTree([float('inf')] * (M + 1), segfunc, ide_ele) # セグ木立てる

# codeforces round716 D - Cut and Stick
# こういうモノイドも乗る

#####segfunc#####
# 範囲内の過半数を占める要素がありそうならその可能性を返すセグ木
# [1, 2, 3, 3]
# [1, 2]について過半数を占める要素なし (-1, 0)
# [3, 3]について過半数を占める要素は3
# (-1, 0)について、3の数は多かったとしても半分
# (1, 1)について, 3の数は多かったとしても半分 - 1
def segfunc(x, y):
    if x[0] == y[0]:
        return x[0], x[1] + y[1]
    elif x[1] > y[1]:
        return x[0], x[1] - y[1]
    elif x[1] < y[1]:
        return y[0], y[1] - x[1]
    else:
        return -1, 0
#################

#####ide_ele#####
ide_ele = (-1, 0)
#################

N, M = getNM()
A = getList()
L = [[] for i in range(N + 1)]
for i in range(N):
    L[A[i]].append(i)

# 使い方
A = [(a, 1) for a in A]
seg = SegTree(A, segfunc, ide_ele)

for _ in range(M):
    l, r = getNM()
    l -= 1
    v, c = seg.query(l, r)
    if c == 0:
        print(1)
    else:
        m = bisect_left(L[v], r) - bisect_left(L[v], l)
        print(max(m * 2 + l - r, 1))

# 二分探索セグ木

class SegmentTree():
    def __init__(self, init, unitX, f):
        self.f = f # (X, X) -> X
        self.unitX = unitX
        self.f = f
        if type(init) == int:
            self.n = init
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
        else:
            self.n = len(init)
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            for i in range(self.n-1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2|1])

    def update(self, i, x):
        i += self.n
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1

    def getvalue(self, i):
        return self.X[i + self.n]

    def getrange(self, l, r):
        l += self.n
        r += self.n
        al = self.unitX
        ar = self.unitX
        while l < r:
            if l & 1:
                al = self.f(al, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)

    def max_right(self, l, z):
        if l >= self.n: return self.n
        l += self.n
        s = self.unitX
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not z(self.f(s, self.X[l])):
                while l < self.n:
                    l *= 2
                    if z(self.f(s, self.X[l])):
                        s = self.f(s, self.X[l])
                        l += 1
                return l - self.n
            s = self.f(s, self.X[l])
            l += 1
            if l & -l == l: break
        return self.n

    def min_left(self, r, z):
        if r <= 0: return 0
        r += self.n
        s = self.unitX
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.f(self.X[l], s)):
                while r < self.n:
                    r = r * 2 + 1
                    if z(self.f(self.X[l], s)):
                        s = self.f(self.X[l], s)
                        r -= 1
                return r + 1 - self.n
            s = self.f(self.X[r], s)
            if r & -r == r: break
        return 0

N, Q = map(int, input().split())
A = [int(a) for a in input().split()]
st = SegmentTree(A, 0, max)
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        st.update(a - 1, b)
    elif t == 2:
        print(st.getrange(a - 1, b))
    else:
        z = lambda x: x < b
        print(min(N, st.max_right(a - 1, z)) + 1)
