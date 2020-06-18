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

N = 4
query = [
[0, 1, 1],
[1, 2, 2],
[2, 3, 4]
]

G = [[] for i in range(N)]
for i in range(N - 1):
    s, t, w = query[i]
    G[s].append((t, w))
    G[t].append((s, w))


def bfs(s):
    dist = [-1] * N
    que = deque([s])
    dist[s] = 0

    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in G[v]:
            if dist[w] >= 0:
                continue
            dist[w] = d + c
            que.append(w)
    d = max(dist)
    # 全部並べて一番値がでかいやつ
    return dist.index(d), d

u, _ = bfs(0)
v, d = bfs(u)

print(d)
