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
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

N = 4
R = 4

query = [
[1, 2, 100],
[1, 4, 200],
[2, 3, 250],
[2, 4, 200],
[3, 4, 100]
]

def build_tree_dis(N, edge_list):

    G = [[] for i in range(N)]

    for i in range(len(edge_list)):
        a, b, c = edge_list[i]
        G[a - 1].append([b - 1, c])
        G[b - 1].append([a - 1, c])

    # 葉（末端の数）
    leaves = []
    for i in range(N):
        if len(G[i]) == 1:
            leaves.append(i)

    return G

edges = build_tree_dis(N, query)

def dij(start, goal):
    dist = [float('inf') for i in range(N)]
    dist_sec = [float('inf') for i in range(N)]
    dist[start] = 0

    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heapq.heappop(pq)
        # 制限緩和
        if d > dist_sec[now]:
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
            # ２番目の最短路
            if dist[i[0]] < d + i[1] < dist_sec[i[0]]:
                dist_sec[i[0]] = d + i[1]
                heapq.heappush(pq, (dist_sec[i[0]], i[0]))
    return dist_sec

# 0から2への最短路は0→1→0→1
print(dij(0, 3))
