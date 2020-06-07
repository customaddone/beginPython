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

N = 4
A = [2, 5, 4, 6]
dp = [[0] * 61 for i in range(N + 1)]

A_alta = [0]
for i in range(N):
    A_alta.append(A[i] + A_alta[i])
print(A_alta)

def splitbit(i, n):
    for j in range(61):
        if n & (1 << j):
            dp[i][j] += 1

for i in range(N):
    splitbit(i + 1, A[i])

# i番目の数字まででのi桁目でのフラグの数
for i in range(1, N):
    for j in range(61):
        dp[i + 1][j] += dp[i][j]

def rang_xor(sta, end):
    cnt = 0
    for i in range(61):
        opt = dp[end + 1][i] - dp[sta][i]
        if opt % 2 != 0:
            cnt += 2 ** i
    return cnt
print(rang_xor(0, 3))
