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

N, C = getNM()
D = [getList() for i in range(C)]
maze = [getList() for i in range(N)]

lis = [[0] * C for i in range(3)]

for i in range(N):
    for j in range(N):
        lis[(i + j) % 3][maze[i][j] - 1] += 1

ans = float('inf')
for vi in permutations([i for i in range(C)], 3):
    opt_0, opt_1, opt_2 = vi
    cnt = 0
    for i in range(C):
        cnt += lis[0][i] * D[i][opt_0]
        cnt += lis[1][i] * D[i][opt_1]
        cnt += lis[2][i] * D[i][opt_2]
    ans = min(ans, cnt)
print(ans)
