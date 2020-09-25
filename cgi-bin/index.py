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

# ABC022 C - Blue Bird
# 自分の家からスタートして同じ道を通らないで家に戻ってくる
# 違う道を通る、一つ目の家と最後の家は違うということ
# ワーシャルフロイドで

N, M = getNM()
query = [getList() for i in range(M)]

dist = [[float('inf')] * N for i in range(N)]
sec_list = []

for i in range(M):
    a, b, c = query[i]
    if a == 1:
        sec_list.append([b - 1, c])
    elif b == 1:
        sec_list.appedn([a - 1, c])
    if a != 1 and b != 1:
        dist[a - 1][b - 1] = c
        dist[b - 1][a - 1] = c

def warshall_floyd(dist):
    for k in range(N):
        # i:start j:goal k:中間地点でループ回す
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

warshall_floyd(dist)

# 高橋くんの家の隣にある家同志について探索
ans = float('inf')
for i in range(len(sec_list)):
    for j in range(i + 1, len(sec_list)):
        x1 = sec_list[i]
        x2 = sec_list[j]
        opt = x1[1] + x2[1] + dist[x1[0]][x2[0]]
        ans = min(ans, opt)

if ans == float('inf'):
    print(-1)
else:
    print(ans)

# ABC051 D - Candidates of No Shortest Paths

N, M = getNM()
query = [getList() for i in range(M)]

dist = [[float('inf')] * N for i in range(N)]
for i in range(N):
    dist[i][i] = 0
for i in range(M):
    a, b, c = query[i]
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c

warshall_floyd(dist)
ng_dist = [0] * M

# 各エッジについて探索
# dist(s, i) + edge(i, j) = dist(s, j)ならその辺は最短距離を構成する
for i in range(N):
    for j in range(M):
        s, t, c = query[j]
        if dist[i][s - 1] + c == dist[i][t - 1]:
            ng_dist[j] = 1

cnt = 0
for i in ng_dist:
    if i == 0:
        cnt += 1
print(cnt)

# ABC073 D - joisino's travel
# Rが小さいのでpermutationする
N, M, R = getNM()

d = [[float("inf")] * N for i in range(N)]
list_R = [int(i) - 1 for i in input().split()]
for i in range(M):
   x, y, z = getNM()
   d[x - 1][y - 1] = min(d[x - 1][y - 1], z)
   d[y - 1][x - 1] = min(d[x - 1][y - 1], z)

warshall_floyd(d)

ans = float('inf')
for case in permutations(list_R):
    x1 = case[0]
    opt = 0
    for j in range(1, R):
        x2 = case[j]
        opt += d[x1][x2]
        x1 = x2
    ans = min(ans, opt)
print(ans)
