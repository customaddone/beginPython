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
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

N, M, T = 8, 15, 120
A = [1, 2, 6, 16, 1, 3, 11, 9]
query = [
[1, 8, 1],
[7, 3, 14],
[8, 2, 13],
[3, 5, 4],
[5, 7, 5],
[6, 4, 1],
[6, 8, 17],
[7, 8, 5],
[1, 4, 2],
[4, 7, 1],
[6, 1, 3],
[3, 1, 10],
[2, 6, 5],
[2, 4, 12],
[5, 1, 30]
]
dist_1 = []
dist_2 = []
for i in range(M):
    a, b, c = query[i]
    dist_1.append([a, b, c])
    # 帰りがけの最短経路については全ての道を逆順にすればいい
    dist_2.append([b, a, c])

def build_tree_dis(N, edge_list):

    G = [[] for i in range(N)]

    for i in range(len(edge_list)):
        a, b, c = edge_list[i]
        G[a - 1].append([b - 1, c])

    # 葉（末端の数）
    leaves = []
    for i in range(N):
        if len(G[i]) == 1:
            leaves.append(i)

    return G

edges_1 = build_tree_dis(N, dist_1)
edges_2 = build_tree_dis(N, dist_2)

def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heapq.heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
    return dist

dij_to = dij(0, edges_1)
dij_from = dij(0, edges_2)
ans = 0

for i in range(N):
    time = dij_to[i] + dij_from[i]
    opt = (T - time) * A[i]
    ans = max(ans, opt)
print(ans)
