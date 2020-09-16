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

N, M, L = getNM()
edges = [getList() for i in range(M)]
Q = getN()
query = [getList() for i in range(Q)]

dist = [[float('inf')] * N for i in range(N)]
for i in range(N):
    dist[i][i] = 0
for i in range(M):
    a, b, c = edges[i]
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c

def warshall_floyd(dist):
    for k in range(N):
        # i:start j:goal k:中間地点でループ回す
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# まず一回回す
warshall_floyd(dist)

# distの抽象化
# edgesの張り替え
dist_alta = [[float('inf')] * N for i in range(N)]
for i in range(N):
    for j in range(i, N):
        if i == j:
            dist_alta[i][j] = 0
            continue
        if dist[i][j] <= L:
            dist_alta[i][j] = 1
            dist_alta[j][i] = 1

warshall_floyd(dist_alta)

for s, t in query:
    if dist_alta[s - 1][t - 1] == float('inf'):
        print(-1)
        continue
    print(dist_alta[s - 1][t - 1] - 1)
