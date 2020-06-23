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

n = 14
w = [8, 7, 1, 4, 3, 5, 4, 1, 6, 8, 10, 4, 6, 5]
# 未開発の部分は-1
dp = [[-1] * (n + 1) for i in range(n + 1)]

# ここに条件を入力
def judge(a, b):
    return abs(w[a] - w[b]) <= 1

def rec(l, r):
    if dp[l][r] != -1:
        return dp[l][r]

    if abs(l - r) <= 1:
        return 0

    res = 0

    # 端っこの２つについて条件が成立する & 間の全てについて条件が成立する
    if judge(l, r - 1) and rec(l + 1,r - 1) == r - l - 2:
        res = r - l

    for i in range(l + 1, r):
        res = max(res, rec(l, i) + rec(i, r))
    dp[l][r] = res
    return res

print(rec(0, n))

S = '11011001'
N = len(S)

dp = [[-1] * (N + 1) for i in range(N + 1)]

def judge_2(a, b):
    return S[a] != S[b]

def rec_2(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if abs(l - r) <= 1:
        return 0

    res = 0
    if judge_2(l, r - 1) and rec_2(l + 1, r - 1) == r - l - 2:
        res = r - l
    for i in range(l + 1, r):
        res = max(res, rec_2(l, i) + rec_2(i, r))
    dp[l][r] = res
    return res

print(rec_2(0, N))
