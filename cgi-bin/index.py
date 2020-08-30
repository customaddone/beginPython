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

# 頂点1から頂点kまでの最短パス上
# ルートはO(n)で求められる
N = getN()
A = getList()
query = [getList() for i in range(N - 1)]

dist = [[] for i in range(N)]
for i in range(N - 1):
    a, b = query[i]
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

ignore = [0] * N
ignore[0] = 1
lis = [A[0]]
rec = [0] * N
rec[0] = 1

# 行きがけ帰りがけの要領
def dfs(u):
    global lis
    for i in dist[u]:
        if ignore[i] != 1:
            ignore[i] = 1
            # 巻き戻し用
            plus = 0 # true or false
            change = (0, 0, 0) # true or false, 変更した場所、変更した数値

            if A[i] > lis[-1]:
                lis.append(A[i])
                plus = 1
            else:
                index = bisect_left(lis, A[i])
                change = (1, index, lis[index])
                lis[index] = A[i]
            rec[i] = len(lis)
            dfs(i)
            # 巻き戻す
            if plus:
                lis.pop()
            else:
                lis[change[1]] = change[2]

dfs(0)
for i in rec:
    print(i)
