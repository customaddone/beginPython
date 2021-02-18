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
    ignore = [-1] * N
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
