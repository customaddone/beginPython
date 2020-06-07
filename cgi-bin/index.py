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
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

# 3人、5回修行できる
N, K = getNM()
# 消化コスト
A = getList()
# 食べにくさ
F = getList()

A.sort()
F.sort(reverse = True)

ng = -1
ok = 10 ** 12 + 1

def judge(limit):
    cnt = 0
    for i in range(N):
        # limit // F[i] 消費コストとして許される値
        # A[i] - (limit // F[i]) 消費コストとして許される値との差
        cnt += max(0, A[i] - (limit // F[i]))
    return cnt

while ok - ng > 1:
    mid = (ok + ng) // 2
    margin = judge(mid)

    # 差がK以下であれば修正可能
    # もうちょい下のmidも試してみる
    if K >= margin:
        ok = mid
    else:
        ng = mid
print(ok)
