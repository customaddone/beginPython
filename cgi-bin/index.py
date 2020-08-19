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
from heapq import heappop, heappush
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

A = [3, 4, -8]
# array内の連続する区間の総和
def imos_sum(A):
    n = len(A)
    imos = [0]
    for i in range(n):
        imos.append(imos[i] + A[i])
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(imos[j] - imos[i])
imos_sum(A)

# roopする配列の長さk以下の区間和
def roop_imos(array, k):
    n = len(array)
    alta = copy.deepcopy(array)
    alta += alta
    imos = [0]
    for i in range(len(alta)):
        imos.append(imos[i] + alta[i])
    for i in range(n):
        for j in range(1, k + 1):
            print(imos[i + j] - imos[i])
# roop_imos(A, 2)
