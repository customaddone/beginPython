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

N, M, D = getNM()
A = getList()
A = [x - 1 for x in A]

# 1回阿弥陀を試してみる
amida = [i for i in range(N)]
for i in range(M):
    a1 = amida[A[i]]
    a2 = amida[A[i] + 1]
    amida[A[i]] = a2
    amida[A[i] + 1] = a1

# 逆にする
amida_alta = [0] * N
for i in range(N):
    amida_alta[amida[i]] = i

# ダブリング
logk = D.bit_length()

doubling = [[-1] * N for _ in range(logk)]

for i in range(N):
    doubling[0][i] = amida_alta[i]

for i in range(1, logk):
    for j in range(N):
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

ans = [i for i in range(N)]
for i in range(logk):
    for j in range(N):
        if D & (1 << i):
            ans[j] = doubling[i][ans[j]]

for i in range(N):
    print(ans[i] + 1)
