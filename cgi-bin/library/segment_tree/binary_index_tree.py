
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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

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

# 二分探索木
# binary search tree
class BST:
    # arrayでどんな値が来るか読み込ませる
    # arrayはソートした配列をいれてね
    def __init__(self, N, array):
        self.N = N
        self.bit = [0] * (N + 1)
        self.comp = {} # value → index
        self.rev = {} # index → value
        for i, a in enumerate(array):
            self.comp[a] = i + 1
            self.rev[i + 1] = a
        self.b = 1 << N.bit_length() - 1

    # 追加 1-indexで収納される
    def add(self, a):
        x = self.comp[a]
        while(x <= self.N):
            self.bit[x] += 1
            x += x & -x

    # 削除
    def erase(self, a):
        x = self.comp[a]
        while(x <= self.N):
            self.bit[x] += -1
            x += x & -x

    def lowerbound(self, w):
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

    # x番目の値を返す
    def query(self, x):
        ind = self.lowerbound(x)
        return self.rev[ind]

# 使い方
# 例: ARC033 C - データ構造
Q = getN()
# ①まずクエリ先読みで使用する値をBSTに読み込ませる
read = []
que = []
for i in range(Q):
    t, x = getNM()
    if t == 1:
        read.append(x)
    que.append([t, x])
bit = BST(len(read), sorted(read))

for t, x in que:
    if t == 1:
        # ②addで値を1つ追加、eraseで消去
        bit.add(x)
    else:
        # ③queryで小さい方からx番目の値を返す
        res = bit.query(x)
        print(res)
        bit.erase(res)
