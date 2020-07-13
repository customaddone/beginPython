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

num = [i for i in range(0, 10, 2)]
A = [2, 4, 5]
B = [2, 3]

for i in A:
    index = bisect_right(num, i)
    print(num[index - 1])

# numの中でのi未満の数字の最大値を求める
for i in A:
    index = bisect_left(num, i)
    print(num[index - 1])

# numの中でのiより大きい数字の最小値を求める
for i in B:
    index = bisect_right(num, i)
    print(num[index])

# numの中でのi以上の数字の最小値を求める
for i in B:
    index = bisect_left(num, i)
    print(num[index])

A = [1, 2, 4, 8, 16, 32]

def or_less(array, x):
    # arrayの中のx以下のものの個数
    # arrayの中のx以下のもののうちの最大値
    index = bisect_right(array, x)
    if index == 0:
        or_less_int = -float('inf')
    else:
        or_less_int = array[index - 1]
    return [index, or_less_int]

def less_than(array, x):
    # arrayの中のx未満のものの個数
    # arrayの中のx未満のもののうちの最大値
    index = bisect_left(array, x)
    if index == 0:
        less_than_int = -float('inf')
    else:
        less_than_int = array[index - 1]
    return [index, less_than_int]

print(or_less(A, 8))
print(less_than(A, 1))

def or_more(array, x):
    # arrayの中のx以上のものの個数
    # arrayの中のx以上のもののうちの最小値
    n = len(array)
    index = bisect_left(array, x)
    if index == n:
        or_more_int = float('inf')
    else:
        or_more_int = array[index]
    return [n - index, or_more_int]

def more_than(array, x):
    # arrayの中のxより大きいものの個数
    # arrayの中のxより大きいのもののうちの最小値
    n = len(array)
    index = bisect_right(array, x)
    if index == n:
        more_than_int = float('inf')
    else:
        more_than_int = array[index]
    return [n - index, more_than_int]

print(or_more(A, 32))
print(more_than(A, 1))
