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

N = getN()

memo = [{} for i in range(N + 1)]

def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]
        if ''.join(t).count('AGC') >= 1:
            return False
    return True

def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]

    if cur == N:
        return 1
    res = 0
    for s in 'AGCT':
        if ok(last3 + s):
            res = (res + dfs(cur + 1, last3[1:] + s)) % mod
    memo[cur][last3] = res
    return res
print(dfs(0, 'TTT'))
