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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
NケースのうちMケースでTLEする
Mケースだけ1/2の確率で正解する
一回で通る確率1/2 ** M
一回で通らない確率1 - (1/2 ** M)
これが続く
1/2 ** M = tと置くと
一回で通る確率　t
二回で通る確率　(1 - t) * t
三回で通る確率　(1 - t) ** 2 * t... これの総和
n回で通る分の期待値 n * (1 - t) ** (n - 1) * t
n+1回で通る分の期待値 (n + 1) * (1 - t) ** n * t
回答に失敗した場合、またイーブンからスタートする
求める期待値をyとすると、y = x + (1 - p)y
"""

N, M = getNM()
total = 1900 * M + 100 * (N - M)
print(total * (2 ** M))
