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
X = getList()

dp = [float('inf')] * (1 << 16)
dp[0] = 0

for bit_state in range(1 << 16):
    for i in range(1, 16):
        cnt = 0
        tmp = 0
        if (1 << (i - 1)) & bit_state:
            cnt += 1
            # bit_stateから(1 << (i - 1))のフラグを消したもの
            tmp += (1 / 3) * dp[~(1 << (i - 1)) & bit_state]
        if (1 << i) & bit_state:
            cnt += 1
            tmp += (1 / 3) * dp[~(1 << (i)) & bit_state]
        if (1 << (i + 1)) & bit_state:
            cnt += 1
            tmp += (1 / 3) * dp[~(1 << (i + 1)) & bit_state]
        if cnt != 0:
            dp[bit_state] = min((tmp + cnt / 3 + (3 - cnt) / 3) * 3 / cnt, dp[bit_state])

ans_state = 0
for i in X:
    ans_state += (1 << i)
print(dp[ans_state])
