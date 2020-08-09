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
import heapq
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    # a - 1の場所にwを追加する
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

    # 区間[l, r - 2]についての合計を求める
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

# BITは前から置いていく
# そのためのクエリソート
N, Q = getNM()
C = getList()
que = [getList() for i in range(Q)]

# que[r]に[l(始点), i(queでのインデックス)]をappend
que_d = defaultdict(list)
for i in range(Q):
    que_d[que[i][1]].append([que[i][0], i])
ans = [0] * Q
# 色iのうち最も右側にあるものはどこにあるか
dic = defaultdict(lambda: -float('inf'))
bit = BIT(N)

for i in range(N):
    # 既に場所が登録されているならそれを削除する
    if dic[C[i]] >= 1:
        bit.add(dic[C[i]], -1)
    # 新しい「良い球」の場所を登録
    # 1-indexで!!
    dic[C[i]] = i + 1
    bit.add(dic[C[i]], 1)

    # queryに答える
    if len(que_d[i + 1]) > 0:
        # 終点rがi + 1であるqueryに答える
        for l, j in que_d[i + 1]:
            # cum(l, r):区間[l - 1, r - 2](0-index)についての合計を求める
            # lは1-indexだがi(r - 1)は0 - index
            ans[j] = bit.cum(l, i + 2)

for i in ans:
    print(i)
