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
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

import sys
sys.setrecursionlimit(1000000)
class LCA(object):
    def __init__(self, G, root=0):
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.go = [] # 行きがけ
        # self.go_dict = {}
        self.back = [] # 帰りがけ
        self.back_dict = {}
        self.bfs()
        self.doubling()

    def bfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.G[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

    def dfs(self, u, p):

        # self.go_dict[u] = len(self.go)
        self.go.append(u)
        for v in E[u]:
            if v != p:
                self.dfs(v, u)
        self.back_dict[u] = len(self.back)
        self.back.append(u)

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

    def get(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        du = self.depth[u]
        dv = self.depth[v]

        for i in range(self.logn):  # depthの差分だけuを遡らせる
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        if u == v: return u  # 高さ揃えた時点で一致してたら終わり

        for i in range(self.logn - 1, -1, -1):  # そうでなければ上から二分探索
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]

    def distance(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.get(u, v)]

    # dfsの帰りがけ順の列があれば深さが深い順に各頂点をマージする方法を教えてくれる
    # [[マージ元1, マージ元2, マージ先],...]
    def unite(self, ar):
        # dfsの行きがけ順にソート
        v_l = [[self.back_dict[v - 1], v - 1] for v in ar]
        v_l.sort(reverse = True)
        bef = []
        aft = [v[1] for v in v_l] # popできるよう逆にする
        res = []

        while len(aft) > 1:
            now = aft.pop()
            while bef and self.depth[lca.get(bef[-1], now)] >= self.depth[self.get(now, aft[-1])]:
                res.append([bef[-1], now]) # 記録1 マージ元
                now = self.get(bef.pop(), now) # nowとbef[-1]を統合して新しい点を作成
                res[-1].append(now) # 記録2 マージ先

            # 一旦保留
            bef.append(now)

        # 残った奴をマージしていく
        now = aft[0]
        while bef:
            res.append([bef[-1], now])
            now = self.get(bef.pop(), now) # nowとbef[-1]を統合して新しい点を作成
            res[-1].append(now)

        return res

# 使い方 ABC014 閉路
n = getN()
G = [[] for _ in range(n)]
for x, y in [getNM() for i in range(n - 1)]:
    G[x - 1] += [y - 1]
    G[y - 1] += [x - 1]

lca = LCA(G)
q = getN()
ans = []
for a, b in [getNM() for i in range(q)]:
    # 根からのaの深さ + 根からのbの深さ - 2 * ダブった部分
    # lca.get(a - 1, b - 1):aとbのlca
    ans += [lca.depth[a - 1] + lca.depth[b - 1] - 2 * lca.depth[lca.get(a - 1, b - 1)] + 1]

print(*ans, sep='\n')

# 典型90問 035 - Preserve Connectivity

N = getN()
E = [[] for i in range(N)]
for i in range(N - 1):
    a, b = getNM()
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

Q = getN()
lca = LCA(E)
# dfsの行きがけ順
lca.dfs(0, -1)

for _ in range(Q):
    k, *v_l = getList()
    cnt = 0
    for a, b, _ in lca.unite(v_l):
        cnt += lca.distance(a, b)
    print(cnt)
