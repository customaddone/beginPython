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
from math import sqrt, pi
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

# [1, 2, 3, 4, 5, 6]について
# K回目の操作の時にk = K // 5とすると
# k番目のものとk + 1番目のものを入れ替える

# 1と2を入れ替える
# 1（2番目に変わった)と3を入れ替える
# 1と4, 1と5

# N回操作した時の状態を求める

# 複数回行う操作について
# これは収束するか？　→　収束（ループ）する
# スタートの状態と30回施行後の状態が同じ

N = getN()
L = ['1', '2', '3', '4', '5', '6']

# 端数については実際に施行する
for i in range(N % 30):
    x1 = L[i % 5]
    x2 = L[(i % 5) + 1]
    L[i % 5] = x2
    L[(i % 5) + 1] = x1
print(''.join(L))
