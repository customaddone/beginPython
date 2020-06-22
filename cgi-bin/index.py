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

N, M, Q = 3, 4, 3
query = [
[1, 3, 3, 100],
[1, 2, 2, 10],
[2, 3, 2, 10]
]

# 数列Aについて得点計算
def counter(array):
    cnt = 0
    for i in range(Q):
        A_b = array[query[i][1] - 1]
        A_a = array[query[i][0] - 1]
        c = query[i][2]
        point = query[i][3]

        if A_b - A_a == c:
            cnt += point
    return cnt

ans = 0
# 重複組み合わせを生成
def rep_comb_pow_2(i, array):
    global ans
    if i == N:
        opt = counter(array)
        ans = max(ans, opt)
        return

    # 1スタート
    last = 1
    if len(array) > 0:
        last = array[-1]

    for j in range(last, M + 1):
        new_array = array + [j]
        rep_comb_pow_2(i + 1, new_array)

# 実行
rep_comb_pow_2(0, [])

print(ans)
