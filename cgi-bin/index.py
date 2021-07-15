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
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353

inf = float('inf')
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

# codeforces round731 G. How Many Paths?

# dfs未使用ver
def scc(E):
    n = len(E)
    # rev_Eを作成
    r_E = [[] for i in range(n)]
    for u in range(n):
        for v in E[u]:
            r_E[v].append(u)
    # トポロジカルソート
    fin = [-1] * n
    topo = []
    for u in range(n):
        if fin[u] != -1:
            continue
        stack = [u]
        while stack:
            u = stack[-1]
            if fin[u] == -1:
                fin[u] = 0
                for v in E[u]:
                    if fin[v] != -1:
                        continue
                    stack.append(v)
            else:
                stack.pop()
                if fin[u] == 0:
                    fin[u] = 1
                    topo.append(u)
    # 逆辺でdfs
    res = []
    while topo:
        u = topo.pop()
        if fin[u] != 1: continue
        fin[u] = 2
        cur = [u]
        i = 0
        while i < len(cur):
            u = cur[i]
            for v in r_E[u]:
                if fin[v] == 2: continue
                fin[v] = 2
                cur.append(v)
            i += 1
        res.append(cur)

    g_n = len(res)
    n_e = [[] for i in range(g_n)]
    roop = [0] * g_n
    index = [0] * n
    for u in range(g_n):
        for v in res[u]:
            index[v] = u
    for u in range(N):
        for v in E[u]:
            if index[u] != index[v]:
                n_e[index[u]].append(index[v])
            else:
                roop[index[u]] = 1

    # g_n: グループの個数
    # res: グループに属する頂点は何
    # index: 頂点iはどこに属するか
    # n_e: グループ同士のエッジ
    # roop: ループするか
    return g_n, res, index, n_e, roop

T = getN()
for _ in range(T):
    _ = input()
    N, M = getNM()
    E = [[] for i in range(N)]
    for _ in range(M):
        a, b = getNM()
        E[a - 1].append(b - 1)

    n, group, index, e, roop = scc(E)

    s = index[0]
    dp = [0] * n
    dp[s] += 1
    for u in range(n):
        # 0から到達できる場合
        if dp[u] > 0:
            # ここにループがある場合
            if roop[u] == 1:
                dp[u] += inf
            for v in e[u]:
                dp[v] += dp[u]

    ans = [0] * N
    for i in range(N):
        if dp[index[i]] > 0:
            if dp[index[i]] == 1:
                ans[i] = 1
            elif dp[index[i]] < inf:
                ans[i] = 2
            else:
                ans[i] = -1

    print(*ans)
