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

N, M = 4, 6
weight = [67786, 3497, 44908, 2156, 26230, 86918]
value = [[1, 3, 4], [2], [2, 3, 4], [2, 3, 4], [2], [3]]

# N個のものを全て手に入れるのに必要なコストの最小値
# コストを1にすれば最小個数がわかる
# Nの数が十分に小さいと使用可能
# Mの数が十分小さければMをbitdpする
def get_everything(n, weight, value):
    m = len(weight)
    dp = [float("inf")] * (1 << n)
    dp[0] = 0

    for i in range(m):
        bit = 0
        for item in value[i]:
            bit |= (1 << (item - 1))

        for j in range(1 << n):
            dp[j | bit] = min(dp[j | bit], dp[j] + weight[i])

    return dp[(1 << N) - 1]

ans = get_everything(N, weight, value)
if ans == float("inf"):
    print(-1)
else:
    print(ans)
