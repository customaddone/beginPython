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
# パス中にある~の最大値(DP)やAならばBである、CならばDでない...（複数個ある）
# を満たすTrue/Falseの組合せはあるかを計算する問題（2-SAT）ができる　嬉しい

# 割とMLEになるのでここを調整
sys.setrecursionlimit(1000000)

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

    # label: グループの個数
    # group: 頂点iのグループの番号
    return label, group

# ALPC G-SCC
N, M = getNM()
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = getNM() # 今回は0-index
    edge[a].append(b)

cnt, topo = scc(N, edge)
print(cnt)
ans = [[] for i in range(cnt)]
for v in range(N):
    ans[topo[v]].append(v)
for a in ans:
    print(len(a), *a)

# ARC111 D - Orientation
N, M = getNM()
E = [getList() for i in range(M)]
C = getList()

G = [[] for _ in range(N)]
ans = [0] * M

for i in range(M):
    a, b = E[i]
    a -= 1
    b -= 1
    if C[a] < C[b]:
        ans[i] = '<-'
    elif C[a] > C[b]:
        ans[i] = '->'
    # = の時のみサイクル　これでdfs木を作る
    else:
        G[a].append([i, b])
        G[b].append([i, a])

ignore = [0] * N

### 強連結なサイクルはdfs木で作ろう ###

def dfs(u, p):
    for i, v in G[u]:
        # 記録してないなら
        if ans[i] == 0:
            a, b = E[i]
            a -= 1
            b -= 1
            if u == a:
                ans[i] = '->'
            else:
                ans[i] = '<-'
            if ignore[v] == 0:
                ignore[v] = 1
                dfs(v, u)

###################################

for i in range(N):
    if ignore[i] == 0:
        ignore[i] = 1
        dfs(i, -1)

for a in ans:
    print(a)
