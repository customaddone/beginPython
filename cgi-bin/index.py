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
mod = 998244353

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

# ABC070 D - Transit Tree Path
N = getN()
dist = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b, c = getNM()
    dist[a].append([b, c])
    dist[b].append([a, c])
ignore = [-1] * (N + 1)

# Kからの最短距離をbfsで測る
def distance(sta):
    # 木をKから順にたどる（戻るの禁止）
    pos = deque([sta])

    while len(pos) > 0:
        u = pos.popleft()
        for i in dist[u]:
            if ignore[i[0]] == -1:
                ignore[i[0]] = ignore[u] + i[1]
                pos.append(i[0])

Q, K = getNM()
ignore[K] = 0
distance(K)
# 答えはK~xまでの距離+K~yまでの距離
ans = []
for i in range(Q):
    x, y = getNM()
    ans.append(ignore[x] + ignore[y])
for i in ans:
    print(i)

# ABC087 D - People on a Line

N, M = getNM()
dist = [[] for i in range(N)]
for i in range(M):
    l, r, d = getNM()
    dist[l - 1].append([r - 1, d])
    dist[r - 1].append([l - 1, -d])

dis = [float('inf')] * N

pos = deque([i for i in range(N)])
while len(pos) > 0:
    u = pos.popleft()
    # 始めの第一歩
    if dis[u] == float('inf'):
        dis[u] = 0
    # 行き先の位置が未確定なら確定させる
    # 既に確定しているなら判定
    for to, d in dist[u]:
        if dis[to] == float('inf'):
            dis[to] = dis[u] + d
            # 位置をレコードした頂点を優先的に処理する必要があるためappendleft
            # 例 que = [0, 2, 1], [1, 2, 3]
            # pos = [0, 1, 2] の時
            # dis = [0, -2, 1]でYesになるはず
            # 0を探索, 1の距離をレコードしてappend disは[0, inf, 1]
            # pos = [1, 2, 2]のため次は1を探索
            # dis[1] == infなのでdis[1] = 0にする
            # dis[1] = 0, dis[2] = 1なのでNo
            pos.appendleft(to)
        else:
            if dis[u] + d != dis[to]:
                print('No')
                exit()
print('Yes')

# ABC126 D - Even Relation
# 頂点0からの距離を調べるだけ
N = getN()
edges = [[] for i in range(N)]
for i in range(N - 1):
    u, v, d = getNM()
    edges[u - 1].append([v - 1, d])
    edges[v - 1].append([u - 1, d])

def dij(start):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    while len(pq) > 0:
        d, now = heapq.heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
    return dist

ans = [0] * N
dij_list = dij(0)
for i in range(N):
    if dij_list[i] % 2 == 0:
        ans[i] = 0
    else:
        ans[i] = 1
for i in ans:
    print(i)

# ABC131 E - Friendships
# スターグラフに線を１本ずつ足していくと
N, K = getNM()

def cmb_1(n, r):
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

cnt = cmb_1(N - 1, 2) - K

if cnt < 0:
    print(-1)
    exit()

dist = [[float('inf')] * N for i in range(N)]
for i in range(N):
    dist[i][i] = 0
query = [[1, i] for i in range(2, N + 1)]

for a, b in combinations([i for i in range(2, N + 1)], 2):
    if cnt == 0:
        break
    query.append([a, b])
    cnt -= 1

print(len(query))
for i in query:
    print(*i)

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
