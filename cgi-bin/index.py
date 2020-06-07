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

A, B, X = getNM()

def small_tlit(a, b, x):
    return (2 * b / a) - (2 * x / (a ** 3))

def big_tlit(a, b, x):
    return a * (b ** 2) / (2 * x)

def tan(angle):
    return math.tan(math.radians(angle))

left = 0
right = 90

for _ in range(100):
    mid = (left + right) / 2
    res = 0
    if 2 * X >= (A ** 2) * B:
        res = small_tlit(A, B, X)
    else:
        res = big_tlit(A, B, X)

    if tan(mid) <= res:
        left = mid
    else:
        right = mid
print(right)
