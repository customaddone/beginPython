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

def build_tree(n, edge_list):

    G = [[] for i in range(n)]

    for a, b in edge_list:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    return G

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
def distance(n, edges, sta):
    # 木をKから順にたどる（戻るの禁止）
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

# ABC067 D - Fennec VS. Snuke
N = 12
query = [
[1, 3],
[2, 3],
[3, 4],
[3, 5],
[5, 11],
[6, 12],
[7, 9],
[8, 9],
[9, 10],
[9, 11],
[11, 12]
]

dist = [[] for i in range(N)]
for i in range(N - 1):
    a, b = query[i]
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

# nowからNまでのルート
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

route = router(N, 0, N - 1)
print(route)

# NG以外のところで辿れるところの数
def dfs_ter(sta, ng):
    pos = deque([sta])

    ignore = [0] * N
    for i in ng:
        ignore[i] = 1

    cnt = 0
    while len(pos) > 0:
        u = pos.popleft()
        ignore[u] = 1
        cnt += 1
        for i in dist[u]:
            if ignore[i] != 1:
                pos.append(i)

    return cnt

L = len(route)
fen_ter = route[:(L + 2 - 1) // 2]
snu_ter = route[(L + 2 - 1) // 2:]

fen_ans = dfs_ter(0, snu_ter)

if fen_ans > N - fen_ans:
    print('Fennec')
else:
    print('Snuke')

# ARC037 B - バウムテスト
N, M = 11, 11
query = [
[1, 2],
[1, 3],
[2, 4],
[3, 5],
[4, 6],
[5, 7],
[6, 8],
[7, 9],
[8, 10],
[9, 11],
[10, 11]
]
dist = [[] for i in range(N)]
for i in range(M):
    a, b = query[i]
    a -= 1
    b -= 1
    dist[a].append(b)
    dist[b].append(a)

ignore = [0] * N
ans = 0
# 閉路検出
def search(x, dist):
    global ans
    # 現在の位置とparent
    pos = deque([[x, -1]])
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

# 一つの木の頂点は全て一回のsearchで塗りつぶされる
for i in range(N):
    if ignore[i] == 0:
        search(i, dist)
print(ans)
