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

N, C = getNM()
query = [getList() for i in range(N)]

query_alta = copy.deepcopy(query)
query_alta.sort(reverse = True)

imos_fore = [0]
imos_back = [0]
for i in range(N):
    # 右回り
    imos_fore.append(imos_fore[i] + query[i][1])
    # 左周り
    imos_back.append(imos_back[i] + query_alta[i][1])

imos_fore_back = copy.deepcopy(imos_back)
imos_back_back = copy.deepcopy(imos_fore)

for i in range(1, N + 1):
    imos_fore[i] -= query[i - 1][0]
    imos_back_back[i] -= 2 * query[i - 1][0]
    imos_back[i] -= (C - query_alta[i - 1][0])
    imos_fore_back[i] -= 2 * (C - query_alta[i - 1][0])

for i in range(1, N + 1):
    imos_fore_back[i] = max(imos_fore_back[i], imos_fore_back[i - 1])
    imos_back_back[i] = max(imos_back_back[i], imos_back_back[i - 1])

fore_ans = 0
for i in range(N + 1):
    opt = imos_fore[i] + imos_fore_back[N - i]
    fore_ans = max(fore_ans, opt)

back_ans = 0
for i in range(N + 1):
    opt = imos_back[i] + imos_back_back[N - i]
    back_ans = max(back_ans, opt)

print(max(fore_ans, back_ans))
