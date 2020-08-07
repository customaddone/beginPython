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

N = 7
S = 'BBFBFBB'

def judge(k):
    imos = [0] * N
    if S[0] == 'B':
        imos[0] = 1
    # ひっくり返していく
    for i in range(1, N - k + 1):
        if i < k:
            rev = imos[i - 1]
        else:
            rev = imos[i - 1] - imos[i - k]
        if (S[i] == 'B') ^ (rev % 2):
            imos[i] += 1
        imos[i] += imos[i - 1]

    # 残りのものが合っているか調べる
    for i in range(N - k + 1, N):
        if i < k:
            rev = imos[N - k]
        else:
            rev = imos[N - k] - imos[i - k]
        if (S[i] == 'B') ^ (rev % 2):
            return float('inf')

    return imos[N - k]

K = 0
M = float('inf')
for i in range(1, N + 1):
    opt = judge(i)
    if opt < M:
        M = opt
        K = i
print(K, M)
