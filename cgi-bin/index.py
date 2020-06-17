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
query1 = [
[1, 3, 10],
[2, 4, 20]
]

query2 = [
[2, 3, 3]
]

# 条件
# d[i] <= d[i + 1]
# d[AD] + DL >= d[BL]
# d[AD] + DD <= d[BD]
# 上記のような制約であればグラフの考え方を適用できる

# グラフ問題も
# コストwの辺e = (v, u)について
# d(v) + w >= d(u)
# vからコストwでuまでいけるが、他の道も使うことができる

# 今回の場合
# d(4) + 0 >= d(3), d(3) + 0 >= d(2)...
# d(1) + 10 >= d(3), d(2) + 20 >= d(4)
# d(2) + 3 <= d(3) → d(3) - 3 >= d(2)

# このグラフの最小距離が条件を全て満たす通りとなり、答えとなる最大値となる
# (少しでも周り道するとどれかの条件を満たさなくなる。最短距離で進むことが制約を全て満たす条件)
edges = []
for i in range(N - 1, 1, -1):
    edges.append([i, i - 1, 0])

for i in range(len(query1)):
    a, b, dis = query1[i]
    edges.append([a - 1, b - 1, dis])

for i in range(len(query2)):
    a, b, dis = query2[i]
    edges.append([b - 1, a - 1, -dis])

def bellman(edges, num_v):
    dist = [float('inf') for i in range(num_v)]
    dist[0] = 0

    changed = True
    while changed:
        changed = False
        for edge in edges:
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True

    return dist

print(bellman(edges, N)[-1])
