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

S = 'RRLLLLRLRRLL'
N = len(S)
logk = (10 ** 5).bit_length()

doubling = [[-1] * N for _ in range(logk)]

# １回目の移動
for i in range(N):
    doubling[0][i] = i + 1 if S[i] == "R" else i - 1

# 2 ** k回目の移動
for i in range(1, logk):
    for j in range(N):
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

ans = [0] * N

# 10 ** 5回ぐらい回せば十分
for i in range(N):
    ans[doubling[logk - 1][i]] += 1

print(*ans)
