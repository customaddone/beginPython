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

N = getN()
l = getList()

dp = [[0] * 21 for _ in range(N)]
# 最初の１個が入った状態でスタート
dp[0][l[0]] = 1
# 一つ目飛ばして二つ目からループさせていく
for i in range(1, N - 1):
    for j in range(21):
        if j - l[i] >= 0:
            # dp[i + 1][j]に合流させていく
            # 例 i = 1, j = 11のとこへi = 0, j = 8のとこから追加させる
            dp[i][j] += dp[i - 1][j - l[i]]
        if j + l[i] <= 20:
            dp[i][j] += dp[i - 1][j + l[i]]
#　最後の１個は使わないので(N - 1) - 1
print(dp[N - 2][l[-1]])
