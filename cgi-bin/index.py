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


n, m = getNM()
s = [list(input()) for i in range(n)]

dc = Dinic(n * m + 2)

# 始点、終点とグリッドに辺を貼る
start = n * m
goal = n * m + 1
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            dc.add_edge(start, m * i + j, 1)
        else:
            dc.add_edge(m * i + j, goal, 1)

# グリッド間に辺を貼る
for i in range(n):
    for j in range(m):
        if j + 1 < m and s[i][j] == "." and s[i][j + 1] == ".":
            u, v = m * i + j, m * i + j + 1
            if (i + j) % 2 == 1:
                u, v = v, u
            dc.add_edge(u, v, 1)
        if i + 1 < n and s[i][j] == "." and s[i + 1][j] == ".":
            u, v = m * i + j, m * (i + 1) + j
            if (i + j) % 2 == 1:
                u, v = v, u
            dc.add_edge(u, v, 1)

ans = dc.max_flow(start, goal)

for u in range(n * m + 2):
    for v, cap, _ in dc.graph[u]:
        # [[9, 0, [0, 1, [...]]]]: 0 → 9へ流量0のエッジ、9 → 0へ流量1のエッジ
        ui, uj = divmod(u, m)
        vi, vj = divmod(v, m)
        if (ui + uj) % 2 == 0 and cap == 0 and u != start and u != goal and v != start and v!= goal:
            if ui + 1 == vi:
                s[ui][uj] = "v"
                s[vi][vj] = "^"
            elif ui == vi + 1:
                s[ui][uj] = "^"
                s[vi][vj] = "v"
            elif uj + 1 == vj:
                s[ui][uj] = ">"
                s[vi][vj] = "<"
            elif uj == vj + 1:
                s[ui][uj] = "<"
                s[vi][vj] = ">"

print(ans)
for res in s:
    print("".join(res))
