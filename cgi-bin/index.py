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

def rand_dist(ransize, rantime):
    dist_alta = []
    dist_alta_2 = set()
    while len(dist_alta) < min(rantime, ransize * (ransize - 1) // 2):
        a, b = rand_ints_nodup(1, ransize, 2)
        c = rand_N(1, 10)
        if not (a, b) in dist_alta_2:
            dist_alta.append([a, b, c])
            dist_alta_2.add((a, b))
    return sorted(dist_alta)

N, M = getNM()
S, T = getNM()
S -= 1
T -= 1
query = [getList() for i in range(M)]
"""
N, M = getNM()
S, T = rand_List(1, N, 2)
print(S, T)
S -= 1
T -= 1
query = rand_dist(N, M)
print(query)
"""

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

def dij(start):
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

list_1 = dij(S)
list_2 = dij(T)

ans = float('inf')
for i in range(N):
    if i == S or i == T:
        continue
    if list_1[T] + list_2[i] == list_1[i] or list_2[S] + list_1[i] == list_2[i]:
        continue
    if list_1[i] == list_2[i]:
        ans = i
        break
if ans < mod:
    print(i + 1)
else:
    print(-1)
