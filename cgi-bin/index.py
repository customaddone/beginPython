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

N = 5
K = 3
A = [1, 3, 5, 4, 2]
# [1, 3, 5]の最小値
# [2, 5, 4]の最小値
# [5, 4, 2]の最小値
pos = deque([0])

# posの内部のa1, a2...についてa1 < a2...かつ
# A[a1] < A[a2]...になるように
for i in range(1, K):
    if A[pos[-1]] < A[i]:
        pos.append(i)
    else:
        pos[-1] = i

for i in range(N - K):
    # iを削除してi + Kを入れる
    # もしposの先頭がiなら
    if pos[0] == i:
        pos.popleft()

    if A[pos[-1]] < A[i + K]:
        pos.append(i + K)
    else:
        pos[-1] = i + K
