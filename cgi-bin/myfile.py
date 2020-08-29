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

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

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


# どのように区間を取ればいいか
# 取り除くことを考えないと
# 順番はどうでもいい
N, K, Q = getNM()
# ソート順Aの連続するK個を取りたいが
A = getList()
A = [[i, A[i]] for i in range(N)]
A.sort(key = lambda i: i[1])
key = []
for k, v in A:
    key.append(k)

# 同じグループ内にいるかつグループ全体の長さがK + Q - 1
for i in range(N - K + 1):
    block = key[:i]

    index = [i for i in range(N)]
    for i in block:
        index[i] = -1
    groups = []
    now = []
    for i in range(N):
        if index[i] == -1:
            if len(now) >= K + Q - 1:
                groups.append(now)
        else:
            now.append(index[i])
    if len(now) >= K + Q - 1:
        groups.append(now)
    print(groups)
