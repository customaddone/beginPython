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

N, M = 4, 2
A = [1, 1, 3, 4]
A.sort()

ans = 0
way = 1

fact =[1] #階乗
for i in range(1, N + 1):
    fact.append(fact[i - 1] * i % mod)

facv = [0] * (N + 1) #階乗の逆元
facv[-1] = pow(fact[-1], mod - 2 , mod)

for i in range(N - 1, -1, -1):
    facv[i] = facv[i + 1] * (i + 1) % mod

def cmb(n, r):
    if n < r:
        return 0
    # 計算
    return fact[n] * facv[r] * facv[n - r] % mod

# 6
print(cmb(4, 2))

for i in range(N - 2 + 1):
    min_sum = A[i] * cmb(N - i - 1, M - 1)
    max_sum = A[-i - 1] * cmb(N - i - 1, M - 1)
    ans += (max_sum - min_sum) % mod
print(ans % mod)
