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

# ABC006 D - トランプ挿入ソート
n = getN()
lista = [getList() for i in range(n)]

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

# E - Sequence Decomposing

N = getN()
A = getArray(N)

# Lisだろ
# [2, 1, 4, 5, 3]の場合
# L:[2] 1が入ってきたらappendleft
# L:[1, 2] 4が入ってきたら現在のLの中で4を下回る最も大きいものを更新
# これが最も勿体無くないやり方
# L:[1, 4]

L = deque([A[0]])
for i in A[1:]:
    index = bisect_left(L, i)
    if index == 0:
        L.appendleft(i)
    else:
        L[index - 1] = i
print(len(L))

# 配列ar上の全ての点について[0, i]の単調増加部分列の長さを求める
# O(NlogN)
# ar = [1, 5, 2, 3, 4]
# lis_len(ar) = [1, 2, 2, 3, 4]
# lis_len(A[::-1])[::-1] = [1, 2, 1, 1, 1] # 後ろからlisしたとき
def lis_len(ar):
    n = len(ar)
    l = []
    res = [0] * n
    for i in range(n):
        index = bisect_left(l, ar[i])
        res[i] = index + 1
        if index == len(l):
            l.append(ar[i])
        else:
            l[index] = ar[i]

    return res
