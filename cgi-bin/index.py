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

"""
4 6 3
2 3 4
1 2 4
2 3 3
4 3 1
1 4 1
4 2 2
3 1 6
"""

N, M, R = getNM()

d = [[float("inf")] * N for i in range(N)]
list_R = [int(i) - 1 for i in input().split()]
for i in range(M):
   x, y, z = getNM()
   d[x - 1][y - 1] = min(d[x - 1][y - 1], z)
   d[y - 1][x - 1] = min(d[x - 1][y - 1], z)

dp = [[-1] * N for i in range(1 << N)]
goal = 0
# Rの地点に全てフラグを立てればOK（順番は気にしない）
for i in list_R:
    goal |= (1 << i)


ans = float('inf')
# sが行ったところのdp, vが現在の位置,sumが合計距離
def rec(ns, nv, n_sum):
    global ans

    pos = []
    heapq.heapify(pos)
    heapq.heappush(pos, [n_sum, ns, nv])

    dp = [[-1] * N for i in range(1 << N)]

    while len(pos) > 0:
        sum, s, v = heapq.heappop(pos)
        print([sum, s, v])

        if s & goal == goal:
            ans = min(ans, sum)
            break

        for u in range(N):
            if s & (1 << u) == 0:
                heapq.heappush(pos, [sum + d[v][u], s|(1 << u), u])

for i in range(R):
    index = list_R[i]
    rec((1 << index), index, 0)
print(ans)
