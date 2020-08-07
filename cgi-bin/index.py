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

"""
N = 10
S = 15
A = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]

right = 0
total = 0
ans = 0

# S以上を求める場合にはこの形で
for left in range(N):
    while right < N and total < S:
        total += A[right]
        right += 1
    if total < S:
        break
    print(left, right - 1)

    if left == right:
        right += 1
    total -= A[left]
"""

P = 5
A = [1, 8, 8, 8, 1]
dict = {}
for i in A:
    dict[i] = 0
# 要素の種類数
V = len(dict.items())

# 事象の数をカウント
cnt = 0
right = 0
# １つ目から全ての事象をカバーするまでrightを進める
while right < P:
    if dict[A[right]] == 0:
        cnt += 1
    dict[A[right]] += 1

    if cnt == len(dict.items()):
        break

    right += 1
print(l, r)

l = 0
# 右を一つ進めて左をできる限り進める
for r in range(right + 1, P):
    # 新しく一つ加える
    dict[A[r]] += 1
    while True:
        # もし要素が一つしか無かったら削れない
        if dict[A[l]] == 1:
            break
        dict[A[l]] -= 1
        l += 1
    print(l, r)
