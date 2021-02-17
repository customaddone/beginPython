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

# ABC010 D - 浮気予防

class FordFulkerson:
    def __init__(self, N):
        self.N = N
        self.edge = [[] for i in range(N)] # 各頂点からのエッジ

    # add_edge(出発、到着、量)
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward] # 行きがけのエッジに帰りがけの情報を埋め込む
        self.edge[fr].append(forward) # 行きがけ
        self.edge[to].append(backward) # 帰りがけ

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.edge[v1].append(edge1)
        self.edge[v2].append(edge2)

    # v ~ t にfだけ流してみる
    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used # ignoreを設定
        used[v] = 1 # ignoreを設定
        for e in self.edge[v]:
            w, cap, rev = e
            if cap and not used[w]: # まだ流せる
                d = self.dfs(w, t, min(f, cap)) # さらに下にいくら流れる
                if d:
                    e[1] -= d # forwardの数が減る
                    rev[1] += d # backwardの数が増える
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        f = INF = 10 ** 9 + 7
        N = self.N
        while f:
            self.used = [0] * N # 更新
            f = self.dfs(s, t, INF) # 少しずつ流す
            flow += f
        return flow

N, G, E = getNM()
F = FordFulkerson(N + 1)
P = getList()

for i in range(E):
    u, v = getNM()
    # 両方エッジつけても問題ない
    F.add_edge(u, v, 1)
    F.add_edge(v, u, 1)

# 高橋くんの所に流す
for p in P:
    F.add_edge(p, N, 1)

ans = F.flow(0, N)

print(ans)
