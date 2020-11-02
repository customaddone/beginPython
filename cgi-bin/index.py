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
mod = 998244353

#############
# Main Code #
#############

# プリム法
n = 7
edge = [
[[1, 1]],
[[1, 0], [2, 2], [3, 3], [7, 4]],
[[2, 1], [10, 5]],
[[3, 1], [1, 4], [5, 6]],
[[7, 1], [1, 3], [8, 6], [5, 5]],
[[10, 2], [5, 4]],
[[5, 3], [8, 4]]
]

def prim_heap():
    used = [1] * n #True:未使用

    edgelist = []
    for e in edge[0]:
        heapq.heappush(edgelist,e)

    used[0] = 0
    res = 0

    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        # もし使用済なら飛ばす
        if not used[minedge[1]]:
            continue

        # 距離最小のものを使用する
        # エッジを一つ使うたびに頂点を消す
        # これをN - 1回繰り返す
        v = minedge[1]
        used[v] = 0

        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,e)
        res += minedge[0]

    return res

print(prim_heap())

# クラスカル法

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

V, E = map(int, input().split())
edges = []
for i in range(E):
    s, t, w = map(int, input().split())
    edges.append((w, s, t))
edges.sort()

def kruskal(n, edges):
    U = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not U.same(s, t):
            res += w
            U.union(s, t)
    return res
print(kruskal(V, edges))

# CODE FESTIVAL 2016 qual B C - Gr-idian MST
# クラスカル法的な考え方

"""
HW領域は広い
(H + 1) * (W + 1)個の家がある
辺には道路がある
i ~ i + 1の縦方向の舗装がコストp
j ~ j + 1の横方向の舗装がコストq

最小全域木を作るためのコスト
木になるんだからH * W - 1本舗装する
もちろんダイクストラ無理
2 2
P = [3, 5]
Q = [2, 7]
  _ _
5 _| |
3 _| |
  2  7 これが最小

繋げる点１つにつき辺が１つ - 1c

クラスカル法: コストが小さいものから繋げてU.same

縦と横を代替できる
小さいものから順にグループが繋がるように
[0, 0], [0, 1], [0, 2]は全て繋がってるものとする
これに[1, 0], [1, 1], [1, 2]を繋げるには横棒を引くか縦棒を引き、他の横棒を借りて連結する
縦一行をグループにするのに縦線が必要な訳ではない

a2

a1
   b1   b2 について

一行目のグループを全て繋げるには
    _
a2 |_
a1 |_ か

a2 |_|
a1 | | の２つの方法がある

縦の合計 + 横1本か全て横か
できたら縦と横入れ替えて実施

次のグループを繋げるためには横一本は絶対使う
後の4本は縦（各1本ずつ）横（たくさん）から4本選ぶ

i行目にある点を全て同じグループにし、motherに統合するイメージ

クラスカル法的な考え方だと
PとQを一緒くたにし、小さい順から取っていく
縦/横棒を拾ったら全ての横/縦棒とバトル
バトルに勝った本数を引ける
"""

W, H = getNM()
P = getArray(W)
Q = getArray(H)
P.sort()
Q.sort()

su = sum(P)
opt1 = su # 横線を最初に引いた状態でスタート
P_imos = deepcopy(P)
for i in range(1, W):
    P_imos[i] += P_imos[i - 1]
for i in range(H):
    # Q[i]は一本は必ず使う
    # 残りW本は好きに
    yoko = bisect_left(P, Q[i])
    if yoko == 0: # 縦線より小さいものがなかった
        opt1 += Q[i] * (W + 1)
    else:
        opt1 += P_imos[yoko - 1] + (W + 1 - yoko) * Q[i]

su = sum(Q)
opt2 = su # 縦線を初めに引いて
Q_imos = deepcopy(Q)
for i in range(1, H):
    Q_imos[i] += Q_imos[i - 1]
for i in range(W):
    tate = bisect_left(Q, P[i])
    if tate == 0:
        opt2 += P[i] * (H + 1)
    else:
        opt2 += Q_imos[tate - 1] + (H + 1 - tate) * P[i]

print(min(opt1, opt2))
