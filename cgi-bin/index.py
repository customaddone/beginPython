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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

N = getN()
A = getList()
A = [[A[i], i] for i in range(N)]
A.sort()

ans = 0
check = [0] * N
U = UnionFind(N)

while A:
    now = A[-1][0]
    index = []
    # 同じ数を引き終わるまで引き続ける
    while A and A[-1][0] == now:
        val, ind = A.pop()
        index.append(ind)
        check[ind] = 1

    # uniteする
    for ind in index:
        # 左側と
        if ind > 0 and check[ind - 1] == 1:
            U.union(ind - 1, ind)
        # 右側と
        if ind < N - 1 and check[ind + 1] == 1:
            U.union(ind, ind + 1)

    # 計算
    for ind in index:
        ans = max(ans, now * U.size(ind))

print(ans)
