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

# 全てのボールを全て違う箱に入れる
# 地点からi離れたところに置くためにはi回試行が必要

# 原点pのボールを(s, e)に一列に置くときの試行回数
def counter(s, e, p):
    sp = abs(s - p)
    ep = abs(e - p)
    if e < p:
        return (sp * (sp + 1) // 2) - ((ep - 1) * ep // 2)
    elif s <= p <= e:
        return (sp * (sp + 1) // 2) + (ep * (ep + 1) // 2)
    else:
        return (ep * (ep + 1) // 2) - ((sp - 1) * sp // 2)

# 全範囲を探索すると微妙に間に合わない
# 緑の位置を最初に決めると(-300 ~ 300ぐらいで全探索)、
# 緑がこの位置にある時、赤の最適な置き方は...
# 緑がこの位置にある時、青の最適な置き方は...
# という風にO(n2)で求められる（赤と青は互いに干渉しないため）
