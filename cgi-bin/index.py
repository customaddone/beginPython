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

# p214 evacuation plan
N = 3
M = 4
build = [[-3, 3, 5], [-2, -2, 6], [2, 2, 5]]
shell = [[-1, 1, 3], [1, 1, 4], [-2, -2, 7], [0, -1, 3]]
E = [[3, 1, 1, 0], [0, 0, 6, 0], [0, 3, 0, 2]] # 避難計画　これが最速か？
ball = 0

mcf = MinCostFlow(N + M + 2)
for i in range(N):
    x, y, b = build[i]
    mcf.add_edge(0, i + 1, b, 0)
    ball += b
    for j in range(M):
        p, q, c = shell[j]
        cost = abs(x - p) + abs(y - q) + 1
        mcf.add_edge(i + 1, N + j + 1, c, cost)

for j in range(M):
    p, q, c = shell[j]
    mcf.add_edge(N + j + 1, N + M + 1, c, 0)
# フロー前とフロー後のGを比べるとどこからどこへいくら流れたかが確認できる
edge_bef = deepcopy(mcf.G)
mcf.flow(0, N + M + 1, ball)
edge_aft = mcf.G

optimal = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        optimal[i][j] = edge_bef[i + 1][j + 1][1] - edge_aft[i + 1][j + 1][1]

if E == optimal:
    print('OPTIMAL')
else:
    print('SUBOPTIMAL')
    for i in optimal:
        print(*i)
