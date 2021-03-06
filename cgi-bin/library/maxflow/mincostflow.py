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
    # 最小費用流(ベルマンフォード版、負コストに対応可)
    # 116行目を状況に応じ変更
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
                return -float('inf')

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

# ABC194 D - Shipping Center

N, M, Q = getNM()
C = [getList() for i in range(N)]
B = getList()
que = []
for i in range(Q):
    l, r = getNM()
    que.append([l - 1, r - 1])

for l, r in que:
    mcf = MinCostFlow(N + M + 2)
    # C: 0 ~ N - 1, B, N ~ N + M - 1
    # start: N + M, end: N + M + 1
    for i in range(N):
        # 始点 ~ Ci
        mcf.add_edge(N + M, i, 1, 0)
        for j in range(M):
            # Ci ~ Bi
            if not l <= j <= r and C[i][0] <= B[j]:
                mcf.add_edge(i, N + j, 1, -C[i][1])
    # B ~ 終点
    for j in range(M):
        mcf.add_edge(N + j, N + M + 1, 1, 0)

    ans = 0
    # 一個ずつ流してみる
    for i in range(N):
        res = -mcf.flow(N + M, N + M + 1, 1)
        if res != -INF:
            ans += res
        else:
            break

    print(ans)

# dinic法

class Dinic:
    def __init__(self, n: int):
        self.n = n
        self.INF = 10 ** 9 + 7
        self.graph = [[] for _ in range(n)]

    def add_edge(self, _from: int, to: int, capacity: int):
        """辺の追加
        1. _fromからtoへ向かう容量capacityの辺をグラフに追加する。
        2. toから_fromへ向かう容量0の辺をグラフに追加する。
        """
        forward = [to, capacity, None]
        forward[2] = backward = [_from, 0, forward]
        self.graph[_from].append(forward)
        self.graph[to].append(backward)

    def bfs(self, s: int, t: int):
        """capacityが正の辺のみを通ってsからtに移動可能かどうかBFSで探索する。
        level: sからの最短路の長さ
        """
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            _from = q.popleft()
            for to, capacity, _ in self.graph[_from]:
                if capacity > 0 and self.level[to] < 0:
                    self.level[to] = self.level[_from] + 1
                    q.append(to)

    def dfs(self, _from: int, t: int, f: int) -> int:
        """流量が増加するパスをDFSで探索する。
        BFSによって作られた最短路に従ってfを更新する。
        """
        if _from == t:
            return f
        for edge in self.itr[_from]:
            to, capacity, reverse_edge = edge
            if capacity > 0 and self.level[_from] < self.level[to]:
                d = self.dfs(to, t, min(f, capacity))
                if d > 0:
                    edge[1] -= d
                    reverse_edge[1] += d
                    return d
        return 0

    def max_flow(self, s: int, t: int) -> int:
        """s-tパス上の最大流を求める。計算量: O(|E||V|^2)"""
        flow = 0
        while True:
            self.bfs(s, t)
            if self.level[t] < 0:
                break
            self.itr = list(map(iter, self.graph))
            f = self.dfs(s, t, self.INF)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.INF)
        return flow
