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

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

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
# nが小さい場合に
if N % 2 == 0:
    alta_f = deepcopy(A) # 前から1個目、3個目...を累積和
    alta_b = deepcopy(A) # 後ろから1個目、3個目...を累積和

    for i in range(1, N):
        if i % 2 == 0:
            alta_f[i] += alta_f[i - 2]
        else:
            alta_f[i] = 0

    for i in range(1, N):
        if i % 2 == 0:
            alta_b[-i - 1] += alta_b[-i + 1]
        else:
            alta_b[-i - 1] = 0

    ans = alta_b[1]
    for i in range(0, N, 2):
        if i + 3 < N:
            ans = max(ans, alta_f[i] + alta_b[i + 3])
        else:
            ans = max(ans, alta_f[i])
    print(ans)
else:
    # 奇数の場合
    # 3つ飛ばしを１回もやらない
    opt_l = [A[i] for i in range(N) if i % 2 == 0]
    ans = sum(opt_l) - min(opt_l)

    alta_f = deepcopy(A) # 前から1個目、3個目...を累積和
    alta_b = deepcopy(A) # 後ろから2個目、4個目...を累積和

    # 2回3つ飛ばしができる

    for i in range(1, N):
        if i % 2 == 0:
            alta_f[i] += alta_f[i - 2]
        else:
            alta_f[i] = 0

    for i in range(2, N):
        if i % 2 == 1:
            alta_b[-i - 1] += alta_b[-i + 1]
        else:
            alta_b[-i - 1] = 0
    print(alta_f)
    print(alta_b)
    # 偶数個目だけ取るのを判定
    ans = max(ans, alta_b[1])
    for i in range(0, N - 2, 2):
        if i + 3 < N:
            ans = max(ans, alta_f[i] + alta_b[i + 3])
        else:
            ans = max(ans, alta_f[i])
    print(ans)
