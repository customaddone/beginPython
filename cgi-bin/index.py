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

N, M = 11, 11
query = [
[1, 2],
[1, 3],
[2, 4],
[3, 5],
[4, 6],
[5, 7],
[6, 8],
[7, 9],
[8, 10],
[9, 11],
[10, 11]
]
dist = [[] for i in range(N)]
for i in range(M):
    a, b = query[i]
    a -= 1
    b -= 1
    dist[a].append(b)
    dist[b].append(a)

ignore = [0] * N
ans = 0
# 閉路検出
def search(x, dist):
    global ans
    # 現在の位置とparent
    pos = deque([[x, -1]])
    ignore[x] = 1
    flag = True

    while pos:
        u, parent = pos.popleft()
        for i in dist[u]:
            if i != parent:
                if ignore[i] == 1:
                    flag = False
                    continue
                ignore[i] = 1
                pos.append([i, u])
    if flag:
        ans += 1

# 一つの木の頂点は全て一回のsearchで塗りつぶされる
for i in range(N):
    if ignore[i] == 0:
        search(i, dist)
print(ans)
