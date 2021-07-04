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

# startからの距離を返す
# 計算量は(V + E)logV
# EがV ** 2(完全グラフ)に近づくと使えない

def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heappush(pq, (dist[i[0]], i[0]))
    return dist

# 最短経路へのパス付きダイクストラ
def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]
    parent = [-1] * N

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        di, now = heappop(pq)
        if (di > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                parent[i[0]] = now
                heappush(pq, (dist[i[0]], i[0]))

    return dist, parent

# 最短経路の本数
def counter(sta, E, d):
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
            for i in E[u]:
                if d[i[0]] == d[u] + i[1]:
                    cnt[i[0]] += cnt[u]
                    pos.append(i[0])
    return cnt

# ABC132 E - Hopscotch Addict
# mod?付きダイクストラ
def dij(start, edges, m):
    # 頂点3倍ダイクストラ
    dist = [[float('inf')] * m for i in range(N)]
    dist[start][0] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heappop(pq)
        if (d > dist[now][d % m]):
            continue
        for i in edges[now]:
            # 現在の距離d, 次の距離d + 1
            if dist[i[0]][(d + i[1]) % m] > dist[now][d % m] + i[1]:
                dist[i[0]][(d + i[1]) % m] = dist[now][d % m] + i[1]
                heappush(pq, (dist[i[0]][(d + i[1]) % m], i[0]))

    return dist

# ARC008 THE☆たこ焼き祭り2012
# 完全グラフのダイクストラ
N = 4
mem = [
[0, 0, 300, 10],
[0, 100, 10, 100],
[0, 200, 10, 200],
[0, 300, 10, 300]
]

dis = [float('inf')] * N
edges = []

def calc(x1, y1, x2, y2, speed):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance / speed

# 完全グラフのダイクストラだろうと0(NlogN)で求まる
def dijkstra(n, start):
    dist = [float('inf')] * n
    pos = [(0, start)]
    heapify(pos)
    dist[start] = 0

    while len(pos):
        cost, u = heappop(pos)

        if dist[u] < cost:
            continue
        # エッジは探索のたびに生成していく
        for i in range(N):
            if i == u:
                continue
            opt = calc(mem[i][0], mem[i][1], mem[u][0], mem[u][1], min(mem[u][2], mem[i][3]))
            if dist[u] + opt < dist[i]:
                dist[i] = dist[u] + opt
                heappush(pos, (dist[u] + opt, i))

    return dist

res = dijkstra(N, 0)
res.sort(reverse = True)

ans = 0
for i in range(N - 1):
    ans = max(ans, res[i] + i)

print(ans)

# 二次元ダイクストラ
E = [[[] for i in range(C)] for i in range(R)]
for i in range(R):
    for j in range(C):
        if j < C - 1:
            E[i][j].append([i, j + 1, A[i][j]])
        if j > 0:
            E[i][j].append([i, j - 1, A[i][j - 1]])
        if i < R - 1:
            E[i][j].append([i + 1, j, B[i][j]])

def dijkstra(h, w, start):
    dist = [[float('inf')] * w for i in range(h)]
    pos = [(0, start[0], start[1])]
    heapify(pos)
    dist[start[0]][start[1]] = 0

    while len(pos):
        cost, y, x = heappop(pos)

        if dist[y][x] < cost:
            continue
        # エッジは探索のたびに生成していく
        for ny, nx, c in E[y][x]:
            if dist[ny][nx] > dist[y][x] + c:
                dist[ny][nx] = dist[y][x] + c
                heappush(pos, (dist[y][x] + c, ny, nx))

    return dist
