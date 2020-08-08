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
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

N, H, R, T = 2, 10, 10, 100
g = 10

def judge(time):
    if time < 0:
        return H
    t = sqrt(2 * H / 10)
    k = int(time / t)
    if k % 2 == 0:
        d = time - k * t
        return H - g * d * d / 2
    else:
        d = k * t + t - time
        return H - g * d * d / 2

ans = []
for i in range(N):
    # 一秒ごとにボールを落下させる
    ans.append(judge(T - i))
# ボールは互いにすり抜けるものと考えて良い
ans.sort()
for i in range(N):
    # RはセンチメートルだがHはメートル
    print(ans[i] + (2 * R * i / 100))
