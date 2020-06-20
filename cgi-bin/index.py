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

N, K = 6, 727202214173249351
A = [6, 5, 2, 5, 3, 2]
A = [i - 1 for i in A]

logk = K.bit_length()
doubling = [[-1] * N for _ in range(logk)]

# ダブリング
# 2 ** 0は１つ後の行き先
for i in range(N):
    doubling[0][i] = A[i]
for i in range(1, logk):
    for j in range(N):
        # doubling[i]はdoubling[i - 1]を２回行えばいい
        # doubling[i - 1][j]移動してその座標からまたdoubling[i - 1]移動
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

index = 0
# 各bitごとに移動を行う
for i in range(logk):
    if K & (1 << i):
        index = doubling[i][index]
print(index + 1)
