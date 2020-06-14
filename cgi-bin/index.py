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

# 目標700点
D, G = getNM()
query = []
for i in range(D):
    p, c = getNM()
    query.append([i + 1, p, c])

ans_cnt = float('inf')

for bit in range(1 << D):
    sum = 0
    cnt = 0
    for i in range(D):
        if bit & (1 << i):
            sum += query[i][0] * query[i][1] * 100 + query[i][2]
            cnt += query[i][1]

    if sum < G:
        for j in range(D - 1, -1, -1):
            if not bit & (1 << j):
                left = G - sum
                fire = query[j][0] * 100
                opt = min(query[j][1], (left + fire - 1) // fire)
                sum += opt * query[j][0] * 100
                cnt += opt
                break

    if sum >= G:
        ans_cnt = min(ans_cnt, cnt)

print(ans_cnt)
