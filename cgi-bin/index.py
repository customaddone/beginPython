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

N, M, R = getNM()

d = [[float("inf")] * N for i in range(N)]
list_R = [int(i) - 1 for i in input().split()]
for i in range(M):
   x, y, z = getNM()
   d[x - 1][y - 1] = min(d[x - 1][y - 1], z)
   d[y - 1][x - 1] = min(d[x - 1][y - 1], z)

def warshall_floyd(dist):
    for k in range(N):
        # i:start j:goal k:中間地点でループ回す
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    #return dist

warshall_floyd(d)

ans = float('inf')
# ワーシャルフロイド + 順列全探索
# 全探索するので中間点は無視していい
for case in permutations(list_R):
    x1 = case[0]
    opt = 0
    for j in range(1, R):
        x2 = case[j]
        opt += d[x1][x2]
        x1 = x2
    ans = min(ans, opt)
print(ans)
