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
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
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

N = 7
H = [2, 1, 4, 5, 1, 3, 3]
# H[i]の値が最小値になるとする
# H[i]は谷底でなければならない

L = [0] * N
R = [0] * N
pos = [0]
for i in range(1, N):
    while pos and H[pos[-1]] >= H[i]:
        pos.pop() # 左端を向こう側に追いやる
    if pos:
        L[i] = pos[-1] + 1
    else:
        L[i] = 0
    pos.append(i) # 左端が迫ってくる

pos = [N - 1]
R[N - 1] = N
for i in range(N - 2, -1, -1):
    while pos and H[pos[-1]] >= H[i]:
        pos.pop()
    if pos:
        R[i] = pos[-1]
    else:
        R[i] = N

    pos.append(i)

ans = 0
for i in range(N):
    ans = max(ans, H[i] * (R[i] - L[i]))
print(ans)
