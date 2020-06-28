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

N, A, B = 4, 5, 3
H = [8, 7, 4, 2]

def judge(time, main, sub, hp):
    diff = main - sub
    cnt = 0
    for i in range(len(hp)):
        left = hp[i] - time * sub
        if left > 0:
            cnt += (left + diff - 1) // diff

    return cnt

ok = 10 ** 12 + 1
ng = -1

while ok - ng > 1:
    mid = (ok + ng) // 2
    opt = judge(mid, A, B, H)

    # mid:仮のの回数
    # opt:midを定めた時必要な爆発の回数
    # 仮の回数が必要な回数より多ければokを緩和
    if mid >= opt:
        ok = mid
    else:
        ng = mid
print(ok)
