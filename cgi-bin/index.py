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

N, A, B, C = getNM()
L = getArray(N)

def counter(array):
    if (1 in array) and (2 in array) and (3 in array):
        opt = [0, 0, 0, 0]
        # 合成に10pかかる
        cnt = 0
        for i in range(len(array)):
            if opt[array[i]] > 0:
                cnt += 1
            if array[i] >= 1:
                opt[array[i]] += L[i]

        res = cnt * 10
        res += abs(opt[1] - A)
        res += abs(opt[2] - B)
        res += abs(opt[3] - C)

        return res

    else:
        return float('inf')

ans = float('inf')
def four_pow(i, array):
    global ans
    if i == N:
        ans = min(ans, counter(array))
        return
    # 4 ** Nループ
    for j in range(4):
        new_array = array + [j]
        four_pow(i + 1, new_array)

four_pow(0, [])
print(ans)

"""
4 ** Nループ
N = 5
L = [1, 1, 1, 1, 1]
cnt = 0
def four_pow(i, array):
    global cnt
    if i == N:
        cnt += 1
        return
    # ここの4を変えてrootを変更
    for j in range(4):
        new_array = array + [j]
        four_pow(i + 1, new_array)

four_pow(0, [])
# 1024
print(cnt)
"""
