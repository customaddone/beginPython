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

R, G, B = 267, 294, 165

dp = [[float('inf')] * (R + G + B + 1) for i in range(2001)]
dp[0][R + G + B] = 0

# 残り個数により置くボールの色が変化する
# ボールを置くコストも変化する
def judge(point, ball):
    if ball > G + B:
        return abs(point - (-100))
    elif G + B >= ball > B:
        return abs(point)
    else:
        return abs(100 - point)

print()

for i in range(1, 2001):
    for j in range(R + G + B, -1, -1):
        if j == R + G + B:
            dp[i][j] = dp[i - 1][j]
        else:
            # i - 1000の地点にj + 1ボールを置き,残りはj個
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1] + judge(i - 1000, j + 1))
print(dp[2000][0])
