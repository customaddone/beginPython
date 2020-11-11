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

# CODE FESTIVAL 2017 qual B C - 3 Steps

"""
N頂点の連結な無向グラフがある　M辺既にある(M >= N - 1)
N <= 10 ** 5
一応M <= 10 ** 5なのでダイクストラ使える
辺を追加していく
頂点uから距離3ある（最短距離でなくてもいい）vを取り、直通の辺をプラス
最大でいくつ

辺を追加する度に他の頂点の選択肢は増えるはずだから
parentから3 = childから2]
uのchildでない頂点vに線を引く　そこから
u - vに線を引くと
uのchild - vのchildにも線を引ける
つまりuのchildとvのchildは同じグループであり、互いに線を引ける

M本の辺について順に探索していくか
結局グループは２つにしかならないのでは
頂点1から見た距離
頂点uのchildのどれかと頂点vのchildのどれかに線があれば繋げる

一本ずつ引いていくと最悪N ** 2になる
UnionFindか
1とiはufか
u - vに線を引くと
uのchild - vのchildにも線を引ける

周４の輪ができる
距離３、５、７...の辺はあるか
距離１の場合は既に線がある
奇数長のパスはあるか

二部グラフでなければ偶奇関係なく好きな回数で好きな場所に行ける
"""

N, M = getNM()
Q = [getList() for i in range(M)]

# 1 - indexで
def bipartite(N, M, edges):
    g = defaultdict(list)
    for a, b in edges:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    color = [0] * (N + 1)
    dq = deque([(0, 1)])

    while dq:
        v, c = dq.popleft()
        color[v] = c
        c *= -1
        for nv in g[v]: # 頂点vの各childを調べる
            if color[nv] == 0: # もし未探索なら
                dq.append((nv, c))
            if color[nv] == -c: # もしcolor[nv]がvの色を反転させたものでなければ
                dq = []
                return False, color

    return True, color

res =  bipartite(N, M, Q)
if res[0]:
    nb = res[1].count(1)
    nw = res[1].count(-1)
    print(nb * nw - M)
else:
    print(N * (N - 1) // 2 - M)
