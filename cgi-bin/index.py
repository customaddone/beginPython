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

S = 'aaaaa'
N = len(S)
# i文字目以降で最初に
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alp = {}
for i in range(26):
    alp[alphabet[i]] = i

# i文字目以降で最初に文字sが登場するのは
next = [[-1] * 26 for i in range(N)]
for i in range(N - 1, -1, -1):
    for j in range(26):
        if i == N - 1:
            break
        next[i][j] = next[i + 1][j]
    next[i][alp[S[i]]] = i

dp = [0] * (N + 1) # 1-indexになる
dp[0] = 1
# 配るdpでやる
for i in range(N):
    for j in range(26):
        if next[i][j] == -1:
            continue
        # 0-indexを1-indexに直す
        dp[next[i][j] + 1] += dp[i]
print(sum(dp))
