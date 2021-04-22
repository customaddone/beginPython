from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product
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

# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <E>: 順方向の有向グラフ
# 出力: (<成分数>, <各頂点の成分の番号>)
sys.setrecursionlimit(300000)

def scc(N, E):
    # 逆方向のグラフ
    E_rev = [[] for i in range(N)]
    for u in range(N):
        for v in E[u]:
            E_rev[v].append(u)

    # orderを作る　深い頂点からorderにappendされる
    order = []
    used = [0] * N
    def dfs(u):
        used[u] = 1
        for v in E[u]:
            if not used[v]:
                dfs(v)
        order.append(u)

    # 上で作ったorderを元に有向グラフの末尾から逆行する
    # もしサイクルがあれば行き先がある
    group = [0] * N
    def r_dfs(u, col):
        group[u] = col
        used[u] = 1
        for v in E_rev[u]:
            if not used[v]:
                r_dfs(v, col)
    # order作成
    for i in range(N):
        if not used[i]:
            dfs(i)

    # 初期化
    used = [0] * N
    label = 0
    # 有向グラフの末尾候補から探索していく
    # ラベルの番号の昇順がトポロジカルな順序
    for i in order[::-1]:
        if not used[i]:
            r_dfs(i, label)
            label += 1

    return label, group

N, M = getNM()
edges = [[] for i in range(N)]
for _ in range(M):
    a, b = getNM()
    edges[a - 1].append(b - 1)
# 多重辺がある
for i in range(N):
    edges[i] = list(set(edges[i]))

_, group = scc(N, edges)
cnt = [0] * N
for i in range(N):
    cnt[group[i]] += 1
ans = 0
for i in range(N):
    ans += cnt[i] * (cnt[i] - 1) // 2
print(ans)
