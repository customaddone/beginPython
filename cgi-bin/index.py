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

# 包除原理
N = 100
M = 3
A = [2, 3, 8]
A.sort(reverse = True)
minus = [0] * (N + 1)

ans = 0
# (A & B & C)の個数について調べる
# → A & Bの個数を計算したものから (A & B & C)の個数を引く
for bit in range((1 << M) - 1, 0, -1):
    prim = 1
    for j in range(M):
        if bit & (1 << j):
            prim = prim // math.gcd(prim, A[j]) * A[j] # lcmの計算
    mi = N // prim
    for i in range(prim, N, prim):
        mi -= minus[i]
    if minus[prim] == 0:
        minus[prim] = mi
    ans += mi
print(ans)

# ABC162 E - Sum of gcd of Tuples (Hard)
N,K = getNM()
ans = 0
rec = [0] * (K + 1)

"""
集合A, B, Cについて
A ⊆ B　かつ B ⊆ Cとすると
集合が小さい順から数えて行って
Bを数える時にB -= A
Cを数える時にC -= Aすればダブらない
"""

for X in range(K, 0, -1):
    rec[X] = pow(K // X, N, mod)
    for i in range(2, K // X + 1):
        rec[X] -= rec[i * X] % mod
    ans += (X * rec[X]) % mod
print(ans % mod)
