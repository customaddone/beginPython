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

N, M, Q = 10, 3, 2
query = [
[1, 5],
[2, 8],
[7, 10],
[1, 7],
[3, 10]
]

# l から rまで行く鉄道の数
lr = [[0 for i in range(N + 1)] for j in range(N + 1)]
# l から r以前のどこかまで行く鉄道の数
imos = [[0 for i in range(N + 1)] for j in range(N + 1)]
imos2 = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in query:
    l, r = i
    lr[l][r] += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # j - 1以前のどこかまで行くもの　+ jまで行くもの
        imos[i][j] = imos[i][j - 1] + lr[i][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # i - 1以前のどこかからスタート + iスタート
        imos2[i][j] = imos2[i - 1][j] + lr[i][j]

print(imos2)
