from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

N = 5
# 木グラフ
que = [
[1, 2],
[1, 4],
[2, 3],
[2, 5]
]
# 重みつき
que_dis = [
[1, 2, 2],
[1, 4, 1],
[2, 3, 2],
[2, 5, 1]
]

# 重みなし
def build_tree(n, edge_list):
    G = [[] for i in range(n)]
    for a, b in edge_list:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    return G

# 重みつき
def build_tree_dis(n, edge_list):
    G = [[] for i in range(n)]
    for a, b, c in edge_list:
        G[a - 1].append([b - 1, c])
        G[b - 1].append([a - 1, c])

    return G

# 木の建設
G1 = build_tree(N, que)
G2 = build_tree_dis(N, que_dis)

# 木を探索
def search(n, edges, sta):
    ignore = [0] * N
    ignore[sta] = 1
    pos = deque([sta])
    # 探索
    while len(pos) > 0:
        u = pos.popleft()
        for i in edges[u]:
            if ignore[i] == 0:
                ignore[i] = 1
                pos.append(i)
# [0, 1, 3, 2, 4]
search(N, G1, 0)

# staからの距離
# staからの距離を求めてそのもっとも遠い店からまた距離を求めた時のもっとも遠い店が木の直径
def distance(n, edges, sta):
    ignore = [-1] * N # 距離を求めたいときはfloat('inf')にする
    ignore[sta] = 0
    pos = deque([sta])

    while len(pos) > 0:
        u = pos.popleft()
        for i in edges[u]:
            if ignore[i[0]] == -1:
                ignore[i[0]] = ignore[u] + i[1]
                pos.append(i[0])
    return ignore
# [0, 2, 4, 1, 3]
print(distance(N, G2, 0))

# staからendまでのルート
def router(n, sta, end):
    pos = deque([sta])
    ignore = [0] * n
    path = [0] * n
    path[sta] = -1

    while pos[0] != end:
        u = pos.popleft()
        ignore[u] = 1

        for i in dist[u]:
            if ignore[i] != 1:
                path[i] = u
                pos.append(i)

    route = deque([end])
    while True:
        next = path[route[0]]
        route.appendleft(next)
        if route[0] == sta:
            break

    return list(route)

# staからbfsして親要素を記録
def parents(n, sta, dist):
    pos = deque([sta])
    ignore = [0] * n
    path = [0] * n # 親要素
    path[sta] = -1
    d = [[] for i in range(n)] # 有向辺

    while pos:
        u = pos.popleft()
        ignore[u] = 1

        for i in dist[u]:
            if ignore[i] != 1:
                path[i] = u
                d[u].append(i)
                pos.append(i)

    return path

# dfsで子要素の部分木の大きいを求める
def dfs(u, par):
    res = 1 # 自身のサイズ
    for v in E[u]:
        if v != par:
            size_c = dfs(v, u) # 子方向の部分木のサイズ
            # print(u, size_c, 'c')
            res += size_c
    size_p = N - res # 親方向に伸びる部分木のサイズ
    # print(u, size_p, 'p')
    return res

dfs(0, -1) # 実行

cnt = 0
size = [0] * N # 部分木のサイズ
parents = [-1] * N # 0を根としたときの親
depth = [0] * N # 深さ

# 親と深さと部分木のサイズを保持しておく
def dfs(u, p):
    global cnt, size, parents, depth
    size[u] -= cnt
    cnt += 1
    for v in E[u]:
        if v != p:
            depth[v] = depth[u] + 1
            parents[v] = u
            dfs(v, u)
    size[u] += cnt

ans = 0
# 部分木の色ぬり + 閉路検出
def search(sta, dist):
    global ans
    # 現在の位置とparent
    pos = deque([[sta, -1]])
    ignore[x] = 1
    flag = True

    while pos:
        u, parent = pos.popleft()
        for i in dist[u]:
            if i != parent:
                if ignore[i] == 1:
                    flag = False
                    continue
                ignore[i] = 1
                pos.append([i, u])
    if flag:
        ans += 1

# ABC021 C - 正直者の高橋くん
# 最短経路の本数

N = getN()
a, b = getNM()
M = getN()
dist = [[] for i in range(N)]
for i in range(M):
    x, y = getNM()
    dist[x - 1].append(y - 1)
    dist[y - 1].append(x - 1)

# スタートからの最短距離測定
def distance(sta):
    # 木をstaから順にたどる（戻るの禁止）
    pos = deque([sta])
    ignore = [-1] * N
    ignore[sta] = 0

    while len(pos) > 0:
        u = pos.popleft()
        for i in dist[u]:
            if ignore[i] == -1:
                ignore[i] = ignore[u] + 1
                pos.append(i)

    return ignore

d = distance(a - 1)

# スタートから特定の点まで最短距離で行く通りの数
def counter(sta):
    pos = deque([sta])
    ignore = [0] * N
    cnt = [0] * N
    cnt[sta] = 1

    while len(pos) > 0:
        u = pos.popleft()
        if ignore[u] == 0:
            ignore[u] = 1
            # d[i] == d[u] + 1を満たすuの子ノード全てに
            # 「スタートからuまでの通りの数」をプラス（他のルートからも来る）
            for i in dist[u]:
                if d[i] == d[u] + 1:
                    cnt[i] += cnt[u]
                    pos.append(i)
    return cnt

print(counter(a - 1)[b - 1] % mod)

# 赤黒木
# 距離が3とか5離れている頂点を探せる？
color = [-1] * N
color[s] = 1
que = deque([s]) # 赤スタート

while que:
    u = que.popleft()
    for v in E[u]:
        if color[v] != -1:
            continue
        # 親のmodが1なら2を入れる
        if color[u] == 1:
            color[v] = 2
        else:
            color[v] = 1
        que.append(v)

# dfsによる連結成分分解　木でなくてもいい
# groupを書き込む
ignore = [0] * N
group = [[] for i in range(N)]

def dfs(u, g):
    ignore[u] = 1
    group[g].append(u)
    for v in E[u]:
        if not ignore[v]:
            dfs(v, g)

g = -1
for u in range(N):
    if not ignore[u]:
        g += 1
        dfs(u, g)

# オイラーツアー
N = getN()
E = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = getNM()
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

for i in range(N):
    E[i].sort()

ans = []
def dfs(u, p):
    ans.append(u)
    for v in E[u]:
        if v != p:
            dfs(v, u)
            ans.append(u)
dfs(0, -1)

# bfsでも一回頂点から流す→葉から探索でdfsができる
# codeforces round 693 G. Moving to the Capital
T = getN()
for _ in range(T):
    _ = input()
    N, M = getNM()
    dis1 = [float('inf')] * N
    dis1[0] = 0
    E = [[] for i in range(N)]
    for _ in range(M):
        u, v = getNM()
        E[u - 1].append(v - 1)

    # 距離の計測
    q = deque([0])
    # トポソ順
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in E[u]:
            if dis1[v] > dis1[u] + 1:
                dis1[v] = dis1[u] + 1
                q.append(v)

    dis2 = [float('inf')] * N
    # 葉から探索
    while order:
        u = order.pop()
        for v in E[u]:
            # 逆行
            if dis1[v] <= dis1[u]:
                dis2[u] = min(dis2[u], dis1[v])
            else:
                dis2[u] = min(dis2[u], dis2[v])

    print(*[min(dis1[i], dis2[i]) for i in range(N)])

# Educational Codeforces Round 112 (Rated for Div. 2)
# D. Say No to Palindromes
# 完全二分木のトーナメントの作り方　逆にしていく
# bi(試合数) = 2 ** K - 1
# ind(試合のコード) = bi - (試合のindex)
# dp = [0] * (bi + 1)
# indの子要素（前の試合）はind * 2とind * 2 + 1

K = getN()
S = list(input())
bi = 2 ** K - 1
dp = [0] * (bi + 1)

def rec(mat, result):
    ind = bi - mat# reverse
    S[bi - ind] = result # rewrite
    while ind >= 1:
        # first game
        if ind > bi // 2:
            if S[bi - ind] == '0' or S[bi - ind] == '1':
                dp[ind] = 1
            else:
                dp[ind] = 2
        # second, third...
        else:
            if S[bi - ind] == '0':
                dp[ind] = dp[ind * 2 + 1]
            elif S[bi - ind] == '1':
                dp[ind] = dp[ind * 2]
            else:
                dp[ind] = dp[ind * 2 + 1] + dp[ind * 2]

        ind //= 2

for i in range(bi):
    rec(i, S[i])

Q = getN()
for _ in range(Q):
    m, r = input().split()
    rec(int(m) - 1, r)
    print(dp[1])

# bfs探索した木の復元　もっとも高さが低いもの

N = getN()
A = [i - 1 for i in getList()]
res = 1
E = [[] for i in range(N)] # 1-indexで返す
prev, next, rev = [0], [], 0 # 前の段の要素の数, 現在の段の要素の数、と現在の段の反転数
for i in range(1, N):
    # 反転している　prevの個数 - 1までは許される
    if A[i - 1] > A[i]:
        # これ以上は持てないので段を変える
        if rev + 1 == len(prev):
            res += 1
            prev = next # これは1以上
            rev = 0
            next = []
        else:
            rev += 1

    # 置く
    next.append(A[i])
    E[prev[rev]].append(A[i])

# 葉から探索していく
T = getN()
for _ in range(T):
    _ = input()
    N, K = getNM()
    E = [[] for i in range(N)]
    for i in range(N - 1):
        u, v = getNM()
        E[u - 1].append(v - 1)
        E[v - 1].append(u - 1)

    depth = [1] * N
    # 葉
    q = deque([i for i in range(N) if len(E[i]) == 1])
    # 子要素の数
    order = [len(E[i]) for i in range(N)]

    while q:
        u = q.popleft()
        for v in E[u]:
            order[v] -= 1
            if order[v] == 1:
                q.append(v)
                depth[v] = depth[u] + 1

    print(sum([(d > K) for d in depth]))

# 非再帰dfs
def euler_tour(N, E, sta):
    q = deque([[sta, 1]])
    dis = [-1] * N
    dis[sta] = 0
    par = [-1] * N

    # 例　部分木の大きさを求める
    size = [1] * N

    while q:
        u, f = q.pop()
        if f:
            #### 行きがけ処理をここに書く ###
            # do function
            #############################
            # 帰りがけ用の記録
            q.append([u, 0])
            # 重みつきなら　for v, d in E[u]
            for v in E[u]:
                if dis[v] == -1:
                    # 重みつきならdis[u] + d
                    dis[v] = dis[u] + 1
                    par[v] = u
                    # 次の探索用
                    q.append([v, 1])
                    #### 子に操作するときはここに書く
                    # do function
                    #############################

        else:
            #### 帰りがけ処理をここに書く ###
            # do function
            if u != 0:
                size[par[u]] += size[u]
            #############################

    return size
