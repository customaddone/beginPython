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

class MinCostFlow:
    def __init__(self, n: int):
        """頂点数をnとする。"""
        self.INF = 10 ** 9 + 7
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, _from: int, to: int, capacity: int, cost: int):
        """辺を追加
        1. _fromからtoへ向かう容量capacity、単位コストcostの辺をグラフに追加する。
        2. toから_fromへ向かう容量0、単位コスト-costの辺をグラフに追加する。
        """
        forward = [to, capacity, cost, None]
        forward[3] = backward = [_from, 0, -cost, forward]
        self.graph[_from].append(forward)
        self.graph[to].append(backward)

    def min_cost_flow(self, s: int, t: int, f: int) -> int:
        """s-tパス上に流量fを流すときの最小費用流を求める。
        計算量: O(|F||E|log|V|)
        """
        res = 0
        potential = [0] * self.n
        prv_v = [0] * self.n
        prv_e = [None] * self.n
        while f > 0:
            # ポテンシャルを用いたダイクストラ法
            dist = [self.INF] * self.n
            dist[s] = 0
            q = [(0, s)]  # q = [(sからのコスト, 現在地)]
            while q:
                cost, _from = heappop(q)
                if dist[_from] < cost:
                    continue
                for edge in self.graph[_from]:
                    to, capacity, cost, _ = edge
                    p_diff = potential[_from] - potential[to]
                    if capacity > 0 and dist[_from] + cost + p_diff < dist[to]:
                        dist[to] = dist[_from] + cost + p_diff
                        prv_v[to] = _from
                        prv_e[to] = edge
                        heappush(q, (dist[to], to))

            if dist[t] == self.INF:
                return -1
            for i in range(self.n):
                if dist[i] != self.INF:
                    potential[i] += dist[i]
            d = f
            v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += potential[t] * d
            v = t
            while v != s:
                edge = prv_e[v]
                edge[1] -= d
                edge[3][1] += d
                v = prv_v[v]
        return res


n, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
INF = 10 ** 18


pd = MinCostFlow(n + n + 2)

s = n + n
t = n + n + 1

pd.add_edge(s, t, INF, 0)
for i in range(n):
    pd.add_edge(s, n + i, k, 0)
    pd.add_edge(i, t, k, 0)
for i in range(n):
    for j in range(n):
        pd.add_edge(n + i, j, 1, -a[i][j])

ans = -pd.min_cost_flow(s, t, INF)

res = [["." for i in range(n)] for i in range(n)]
for i in range(n):
    for j, cap, cost, _ in pd.graph[n + i]:
        if 0 <= j <= n and cap == 0:
            res[i][j] = "X"

print(ans)
for r in res:
    print("".join(r))
