from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353

INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

class LCA(object):
    def __init__(self, G, root=0):
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.dfs()
        self.doubling()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.G[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

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

"""
与えられた頂点を全て連結にするには？
小さい例から考える
N, Q <= 5000　なら目的の点の中から適当なのを1つ選んで流す O(N^2)
Kj = 2なら 2頂点のパス長を求める LCAでできる
Kj = 3なら もう一つできる まず2つでLCA 残りの1つは2つとLCAした内の近い方

連結にする頂点の個数は200000以下なのだから 1頂点につきLCA一回で求められれば
左から順にLCAすればいい　左?
どのように並べるか？　左とは？ dfsで順番が求まるはず

近い距離のもの同士で順に繋いでいく　前後のどちらかが一番近いもの
DAGできるか

depthで揃える
"""

N = getN()
E = [[] for i in range(N)]
for i in range(N - 1):
    a, b = getNM()
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

l = []
def dfs(u, p):
    for v in E[u]:
        if v != p:
            dfs(v, u)
    l.append(u)

dfs(0, -1)

Q = getN()
lca = LCA(E)

for _ in range(Q):
    k, *v = getList()
    v = set([i - 1 for i in v])
    prev = deque([i for i in l if i in v])
    # 頂点を1/2ずつにまとめ上げる
    cnt = 0
    while len(prev) > 1:
        s1, s2 = prev.popleft(), prev.popleft()
        now = lca.get(s1,  s2)
        cnt += lca.depth[s1] + lca.depth[s2] - 2 * lca.depth[now]
        next = deque()
        while prev:
            o1 = lca.get(now, prev[0])
            if len(prev) > 1:
                o2 = lca.get(prev[0], prev[1])
            else:
                o2 = 0

            # 統合
            if lca.depth[o1] >= lca.depth[o2]:
                cnt += lca.depth[now] + lca.depth[prev[0]] - 2 * lca.depth[o1]
                prev.popleft()
                now = o1
            # 新規 前のはストックしとく
            else:
                next.append(now)
                cnt += lca.depth[prev[0]] + lca.depth[prev[1]] - 2 * lca.depth[o2]
                prev.popleft()
                prev.popleft()
                now = o2
        # 最後に残っている頂点
        if not (len(next) > 0 and next[-1] == now):
            next.append(now)

        prev = next

    print(cnt)
