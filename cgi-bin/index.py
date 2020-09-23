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

# ABC004 マーブル
# ベルマンフォード式最小

# 全てのボールを全て違う箱に入れる
# 地点からi離れたところに置くためにはi回試行が必要

# 原点pのボールを(s, e)に一列に置くときの試行回数
def counter(s, e, p):
    sp = abs(s - p)
    ep = abs(e - p)
    if e < p:
        return (sp * (sp + 1) // 2) - ((ep - 1) * ep // 2)
    elif s <= p <= e:
        return (sp * (sp + 1) // 2) + (ep * (ep + 1) // 2)
    else:
        return (ep * (ep + 1) // 2) - ((sp - 1) * sp // 2)

# 全範囲を探索すると微妙に間に合わない
# 緑の位置を最初に決めると(-300 ~ 300ぐらいで全探索)、
# 緑がこの位置にある時、赤の最適な置き方は...
# 緑がこの位置にある時、青の最適な置き方は...
# という風にO(n2)で求められる（赤と青は互いに干渉しないため）

class MinCostFlow:
    """ 最小費用流(ベルマンフォード版、負コストに対応可) """

    INF = 10 ** 18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr])-1])

    def flow(self, s, t, f):

        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        prv_v = [0] * N
        prv_e = [0] * N

        while f:
            dist = [INF] * N
            dist[s] = 0
            update = True

            while update:
                update = False
                for v in range(N):
                    if dist[v] == INF:
                        continue
                    for i, (to, cap, cost, _) in enumerate(G[v]):
                        if cap > 0 and dist[to] > dist[v] + cost:
                            dist[to] = dist[v] + cost
                            prv_v[to] = v; prv_e[to] = i
                            update = True
            if dist[t] == INF:
                return -1

            d = f; v = t
            while v != s:
                d = min(d, G[prv_v[v]][prv_e[v]][1])
                v = prv_v[v]
            f -= d
            res += d * dist[t]
            v = t
            while v != s:
                e = G[prv_v[v]][prv_e[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prv_v[v]
        return res

R, G, B = getNM()
N = R + G + B

# 最小費用流
mcf = MinCostFlow(1006)
# 始点からRGBの移動前
# 1001（始点）から1002(赤色原点)へエッジ, R個まで、コスト0
mcf.add_edge(1001, 1002, R, 0)
mcf.add_edge(1001, 1003, G, 0)
mcf.add_edge(1001, 1004, B, 0)

# 0~1000の頂点番号は座標位置と一致させてある
# 各頂点1個まで通れる
for v in range(1001):
    # R => 各座標
    mcf.add_edge(1002, v, 1, abs(400-v))
    # G => 各座標
    mcf.add_edge(1003, v, 1, abs(500-v))
    # B => 各座標
    mcf.add_edge(1004, v, 1, abs(600-v))
    # 各座標 => 終点(1005)
    mcf.add_edge(v, 1005, 1, 0)

# N個のボールを送るための最小費用
print(mcf.flow(1001, 1005, N))
