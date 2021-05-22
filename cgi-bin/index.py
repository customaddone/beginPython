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
sys.setrecursionlimit(1000000)
INF = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

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

# ABC133 F - Colorful Tree

"""
クエリ先読みする
全頂点についてのこれまでの各色の本数と距離は表示することができる
保存はできない
必要な分だけ保存すればいいのでは　→　クエリ先読み
"""

N, Q = getNM()
E = [[] for i in range(N)]
E1 = [[] for i in range(N)]
for _ in range(N - 1):
    a, b, c, d = getNM()
    E[a - 1].append([b - 1, c, d])
    E[b - 1].append([a - 1, c, d])
    E1[a - 1].append(b - 1)
    E1[b - 1].append(a - 1)

que = [] # 先読みする
lca = LCA(E1)
# want[u][c]: [色cの本数、色c分の距離]
# 大して数はない
want = [{} for i in range(N)]
dist = [0] * N # 合計の距離
for _ in range(Q):
    c, add, u, v = getNM()
    u -= 1
    v -= 1
    want[u][c] = [0, 0]
    want[v][c] = [0, 0]
    want[lca.get(u, v)][c] = [0, 0]
    que.append([c, add, u, v])

d_c = defaultdict(int) # 0 ~ xまでの各色の本数
d_d = defaultdict(int) # 0 ~ xまでの各色のsum

# 必要な分だけメモする
def dfs(u, p, su_d):
    global dist
    dist[u] = su_d
    # print(u, p, d_c, d_d)
    for c in want[u].keys():
        want[u][c] = [d_c[c], d_d[c]]
    for v, c, d in E[u]:
        if v != p:
            d_c[c] += 1
            d_d[c] += d
            dfs(v, u, su_d + d)
            d_c[c] -= 1
            d_d[c] -= d

dfs(0, -1, 0)

for c, add, u, v in que:
    rel = lca.get(u, v)
    # 元々の距離
    d1 = dist[u] + dist[v] - 2 * dist[rel]
    # + 色cの本数 * add
    plus = add * (want[u][c][0] + want[v][c][0] - 2 * want[rel][c][0])
    # - 色c分の距離の合計
    minus = want[u][c][1] + want[v][c][1] - 2 * want[rel][c][1]
    print(d1 + plus - minus)
