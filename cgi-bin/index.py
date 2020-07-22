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

b1 = getList()
b2 = getList()
c1 = getList() + [0]
c2 = getList() + [0]
c3 = getList() + [0]
b = b1 + b2
c = c1 + c2 + c3
S = sum(b) + sum(c)

def counter(array):
    male = 0
    for i in range(9):
        # bの得点
        if i <= 5:
            if array[i] == array[i + 3]:
                male += b[i]
        # cの得点
        if i % 3 == 0 or i % 3 == 1:
            if array[i] == array[i + 1]:
                male += c[i]
    return male

memo = {}

def solve(array):
    # メモ呼び出し
    if str(array) in memo:
        return memo[str(array)]
    # ターンの計算
    turn = 1
    for i in array:
        if i == 0 or i == 1:
            turn += 1
    if turn == 10:
        return counter(array)

    if turn % 2 == 0:
        point = S
    else:
        point = -S

    # i番目に駒を置いた時の全通りを探索して最善の手を呼び出す
    for i in range(9):
        if array[i] == -1:
            new = copy.deepcopy(array)
            if turn % 2 == 0:
                new[i] = 1
                point = min(point, solve(new))
            else:
                new[i] = 0
                point = max(point, solve(new))
    memo[str(array)] = point
    return point

opt = [-1] * 9
ans = solve(opt)
print(ans)
print(S - ans)
