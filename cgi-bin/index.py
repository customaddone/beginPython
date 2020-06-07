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

N, K = getNM()
A = getList()
lista = [[0, 0] for i in range(61)]
# bitの各桁が１か０かをlistaに収納
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            lista[i][0] += 1
        else:
            lista[i][1] += 1
for i in A:
    splitbit(i)

ans = 0
cnt = 0
for i in range(60, -1, -1):
    if lista[i][1] > lista[i][0] and cnt + 2 ** i <= K:
        cnt += 2 ** i
        ans += lista[i][1] * 2 ** i
    else:
        ans += lista[i][0] * 2 ** i
print(ans)
