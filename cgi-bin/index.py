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

N = 7
a, b = 1, 7
M = 8
que = [
[1, 2],
[1, 3],
[4, 2],
[4, 3],
[4, 5],
[4, 6],
[7, 5],
[7, 6]
]
dist = [[] for i in range(N)]
for x, y in que:
    dist[x - 1].append(y - 1)
    dist[y - 1].append(x - 1)

# スタートからの最短距離測定
def distance(sta):
    # 木をstaから順にたどる（戻るの禁止）
    pos = deque([sta])
    ignore = [-1] * N
    ignore[sta] = 0

    while len(pos) > 0:
        u = pos.popleft()
        for i in dist[u]:
            if ignore[i] == -1:
                ignore[i] = ignore[u] + 1
                pos.append(i)

    return ignore

d = distance(a - 1)

# スタートから特定の点まで最短距離で行く通りの数
def counter(sta):
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
            for i in dist[u]:
                if d[i] == d[u] + 1:
                    cnt[i] += cnt[u]
                    pos.append(i)
    return cnt

print(counter(a - 1)[b - 1] % mod)
