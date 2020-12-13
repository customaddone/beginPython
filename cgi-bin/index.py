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

# ABC010
# 最小カット問題
# 始点、終点と各点を結びつける
N, G, E = getNM()
P = getList()
query = []
for i in range(E):
    a, b = getNM()
    query.append([a, b, 1])
    query.append([b, a, 1])
# goalへのquery増築
N += 1
for i in range(G):
    query.append([N - 1, P[i], 1])
    query.append([P[i], N - 1, 1])

ans = 0
lines = defaultdict(set)
cost = defaultdict(lambda: defaultdict(int))
for i in range(len(query)):
    a, b, c = query[i]
    if c != 0:
        lines[a].add(b)
        cost[a][b] += c

# 蟻本  p205 asteroid
N = 3
K = 4
que = [
[1, 1],
[1, 3],
[2, 2],
[3, 2]
]

# 始点を0、縦座標rowを1 ~ N, 横座標colをN + 1 ~ 2N, 終点を2N + 1にする
# 1-indexならこれでいい
# 二分グラフの最小点被覆は最大マッチング
# 二分グラフの最大安定集合は上記を除く補集合
dist = []
for i in range(1, N + 1): # 始点、終点
    dist.append([0, i, 1])
    dist.append([i + N, 2 * N + 1, 1])
for a, b in que: # 各惑星について
    dist.append([a, b + N, 1])

N = 2 * N + 2 # 2 * N + 2倍に拡張する
lines = defaultdict(set)
cost = [[0] * N for i in range(N)]
for i in range(len(dist)):
    a, b, c = dist[i]
    lines[a].add(b)
    cost[a][b] += c
ans = 0

# sからスタート
def Ford_Fulkerson(sta, end):
    global ans
    queue = deque()
    queue.append([sta, float('inf')])

    ignore = [1] * N
    ignore[sta] = 0

    route = [0] * N
    route[sta] = -1

    while queue:
        s, flow = queue.pop()
        for t in lines[s]:  #s->t
            if ignore[t]: #未到達
                # flowは入ってくる量、出る量のうち小さい方
                flow = min(cost[s][t], flow)
                route[t] = s
                queue.append([t, flow])
                ignore[t] = 0
                if t == end: #ゴール到達
                    ans += flow
                    break
        else:
            continue #breakされなければWhile節の先頭に戻る
        # Falseはされない
        break
    else:
        return False

    t = end
    s = route[t]
    # goalまで流れた量はflow
    # 逆向きの辺を貼る
    while s != -1:
        #s->tのコスト減少，ゼロになるなら辺を削除
        cost[s][t] -= flow
        if cost[s][t] == 0:
            lines[s].remove(t)
            #t->s(逆順)のコスト増加，元がゼロなら辺を作成
        if cost[t][s] == 0:
            lines[t].add(s)

        cost[t][s] += flow

        # 一つ上の辺をたどる
        t = s
        s = route[t]

    return True

while True:
    # ちょびちょび流して行ってゴールまで流れなくなったら終了
    if Ford_Fulkerson(0, N - 1):
        continue
    else:
        break

print(ans)

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

"""
# N人の人がいます　2人1組になります
# i番目の人とj番目の人がペアになった時、Aij点獲得します
# 得点を最大化してください
# 2 - 4, 4 - 2とならないようにi + 1からjをスタートさせる

4
0 50 -20 10
50 0 30 -40
-20 30 0 60
10 -40 60 0

-110
"""

N = getN()
P = [getList() for i in range(N)]
mcf = MinCostFlow(2 * N + 2)

for i in range(N):
    mcf.add_edge(2 * N, i, 1, 0)
    mcf.add_edge(N + i, 2 * N + 1, 1, 0)

for i in range(N):
    for j in range(i + 1, N):
        if i != j:
            mcf.add_edge(i, N + j, 1, -P[i][j])

print(mcf.flow(2 * N, 2 * N + 1, N // 2))
