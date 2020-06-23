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

N = input()
K = getN()
L = len(N)

def judge(a):
    return a != 0

# N以下の数字で条件を満たす桁がk個のもの
def digit_dp(n, k):
    l = len(n)

    dp = [[[0] * (k + 1) for _ in range(2)] for i in range(l + 1)]
    dp[0][0][0] = 1

    for i in range(l):
        d = int(n[i])

        for j in range(2):
            for d_j in range(10 if j else d + 1):
                for k_j in range(k + 1):
                    # 0じゃない数字が混じっていれば数字は進む
                    if judge(d_j):
                        # 求めたい個数以下なら
                        if k_j + 1 <= k:
                            dp[i + 1][j | (d_j < d)][k_j + 1] += dp[i][j][k_j]
                    else:
                        dp[i + 1][j | (d_j < d)][k_j] += dp[i][j][k_j]

    return dp[l][0][k] + dp[l][1][k]

print(digit_dp(N, K))
