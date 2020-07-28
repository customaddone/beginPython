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

# 条件
# 並び終えた後の山札の集合をD{d1, d2, d3... dn}とすると
# d1 < d2 < d3... dnであること

# c1, c2, c3...の任意のci, cjについて
# i < j の時 ci < cjなら何もしなくていい
# ci > cjの時並び変える必要がある（操作回数 + 1）

# 集合Cから条件を満たす{d1, d2, d3...}をとる中で、長さが最大値になるものを求める

# 類題 AGC024 B - Backfront

# 何もしなくてもいいのはc1 == c2 + 1の時
# 条件
# 並び終えた後の山札の集合をD{d1, d2, d3... dn}とすると
# d1, d1 + 1, d1 + 2...という風に並ぶ集合の長さの最大値を求める

n = getN()
lista = getArray(n)

# 最長増加部分列問題 (LIS)の問題
def lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        # このelseに引っかかった時にトランプのソートが必要
        else:
            L[bisect_left(L, a)] = a
    return len(L)
print(n - lis(lista))
