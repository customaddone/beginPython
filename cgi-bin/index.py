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

n = 7
edge = [
[[1, 1]],
[[1, 0], [2, 2], [3, 3], [7, 4]],
[[2, 1], [10, 5]],
[[3, 1], [1, 4], [5, 6]],
[[7, 1], [1, 3], [8, 6], [5, 5]],
[[10, 2], [5, 4]],
[[5, 3], [8, 4]]
]

def prim_heap():
    used = [1] * n #True:未使用

    edgelist = []
    for e in edge[0]:
        heapq.heappush(edgelist,e)

    used[0] = 0
    res = 0

    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        # もし使用済なら飛ばす
        if not used[minedge[1]]:
            continue

        # 距離最小のものを使用する
        # エッジを一つ使うたびに頂点を消す
        # これをN - 1回繰り返す
        v = minedge[1]
        used[v] = 0

        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,e)
        res += minedge[0]

    return res

print(prim_heap())
