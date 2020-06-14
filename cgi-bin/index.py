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
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

# 約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# [1, 2, 3, 4, 6, 12]
print(make_divisors(12))

# 公約数列挙
def make_divisors(m, n):
    divisors = []
    numi = min(m, n)
    numa = max(m, n)
    for i in range(1, int(math.sqrt(numi)) + 1):
        if numi % i == 0:
            if numa % i == 0:
                divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != numi // i and numa % (numi // i) == 0:
                divisors.append(numi // i)
    return sorted(divisors)
# [1, 2, 3, 6]
print(make_divisors(12, 18))

# 最大公約数
# 6
print(gcd(12, 18))

# 最小公倍数
def lcm(x, y):
    return x * (y // gcd(x, y))

# 36
print(lcm(12, 18))
