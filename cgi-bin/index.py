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

# 典型90 062 - Paint All（★6）
# N個全てのアイテムを使う　つまりどの順番でアイテムを使うか
# ボールiが白いままであれば、Aj = i or Bj = iなアイテムIjを使える
# つまりアイテムiを使うのはこうしたアイテムより後である方がいい
# 最後のボールは必ずAi = i or Bi = iである必要がある

# グラフ問題にできる
# これをAi = i or Bi = iのアイテムから流していって全て巡れるか
# 適当にやるとO(N^2)かかる
# なので上流から流した方がいい　上流？
# →SCCしてトポソするとDAGになるのでやる

# 強連結トポソ
N = getN()
E = [set() for i in range(N)]
P = []
for i in range(N):
    a, b = getNM()
    P.append([a - 1, b - 1])
    E[a - 1].add(i)
    E[b - 1].add(i)
E = [list(i) for i in E]

# トポソ
cnt, topo = scc(N, E)
order = [[] for i in range(cnt)]
for i in range(N):
    order[topo[i]].append(i)

# あとはトポソした通りに流す
ignore = [0] * N
ans = []
for o in order:
    for i in o:
        # そもそもスタート地点じゃない or もう見た
        if (i != P[i][0] and i != P[i][1]) or ignore[i] == 1:
            continue
        # iは未探索なので
        q = deque([i])
        ignore[i] = 1
        ans.append(i)

        while q:
            u = q.popleft()
            for v in E[u]:
                if ignore[v] == 0:
                    # 未探索なら
                    ignore[v] = 1
                    ans.append(v)
                    q.append(v)

if len(ans) == N:
    for a in ans[::-1]:
        print(a + 1)
else:
    print(-1)
