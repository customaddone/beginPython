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
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

# ABC051
N, M = getNM()
query = [getList() for i in range(M)]

dist = [[float('inf')] * N for i in range(N)]
for i in range(N):
    dist[i][i] = 0
for i in range(M):
    a, b, c = query[i]
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
ng_dist = [0] * M

# エッジを調べてそれが地点間最小距離生成の役にたつか
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

# ABC074
N = getN()
query = [getList() for i in range(N)]
query_before = copy.deepcopy(query)

def warshall_floyd(dist):
    for k in range(N):
        # i:start j:goal k:中間地点でループ回す
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

warshall_floyd(query)

if query != query_before:
    print(-1)
    exit()

edges = []
for i in range(N):
    for j in range(i + 1, N):
        edges.append([query[i][j], i, j])

# エッジを調べる
cnt = 0
for i in edges:
    flag = True
    w, s, t = i
    for k in range(N):
        # ここ注意
        if k != s and k != t and w >= query[s][k] + query[k][t]:
            flag = False
            break
    if flag:
        cnt += w
print(cnt)
