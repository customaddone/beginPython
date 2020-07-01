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

A, B, Q = getNM()
# 神社
S = getArray(A)
# 寺
T = getArray(B)
query = getArray(Q)

S.insert(0, -float('inf'))
T.insert(0, -float('inf'))
S.append(float('inf'))
T.append(float('inf'))

def close(data, point):
    west = data[bisect_left(data, point) - 1]
    east = data[bisect_left(data, point)]

    return west, east

for i in range(Q):
    now = query[i]
    shrine_west, shrine_east = close(S, now)
    temple_west, temple_east = close(T, now)

    ww = now - min(shrine_west, temple_west)
    we_1 = (now - shrine_west) * 2 + (temple_east - now)
    we_2 = (now - temple_west) * 2 + (shrine_east - now)
    ee = max(shrine_east, temple_east) - now
    ew_1 = (shrine_east - now) * 2 + (now - temple_west)
    ew_2 = (temple_east - now) * 2 + (now - shrine_west)

    print(min(ww, we_1, we_2, ee, ew_1, ew_2))
