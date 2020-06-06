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
"""
N = rand_N(2, 6)
query = rand_query(2, 10, N)
print(query)
ans_taka, ans_aoki = query[0]
"""

N = getN()
query =  [getList() for i in range(N)]
# 一回目の選挙速報の結果を受けて
ans_taka, ans_aoki = query[0]

# 現在の高橋くん、青木くんの票数、選挙速報の結果の比を基に
# 次の高橋くん、青木くんの票数の最小値が出てくる
def vote(taka, aoki, ratio):
    ratio_taka, ratio_aoki = ratio
    taka_multi = (taka + ratio_taka - 1) // ratio_taka
    aoki_multi = (aoki + ratio_aoki - 1) // ratio_aoki
    multi = max(taka_multi, aoki_multi)

    return [ratio_taka * multi, ratio_aoki * multi]

# 選挙速報２回目〜
for i in range(1, N):
    ans_taka, ans_aoki = vote(ans_taka, ans_aoki, query[i])
    # print(ans_taka, ans_aoki)
print(ans_taka + ans_aoki)
