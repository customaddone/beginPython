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

# 菱形の関数
"""
dp1 = [[0] * C for i in range(R)]
def diam(x, y, size, dp):
    max_x = len(dp[0]) - 1
    max_y = len(dp) - 1
    wid = size - 1
    if wid <= x <= max_x - wid and wid <= y <= max_y - wid:
        for h in range(y - wid, y + wid + 1):
            diff = abs(y - h)
            for w in range(x - (wid - diff), x + (wid - diff) + 1):
                dp[h][w] = 1
"""

R, C, K = getNM()
S = [list(input()) for i in range(R)]
Salta = copy.deepcopy(S)
wid = K - 1

# 菱形状に"X"をつける関数
def diam(x, y, size, dp):
    max_x = len(dp[0]) - 1
    max_y = len(dp) - 1
    for h in range(y - wid, y + wid + 1):
        diff = abs(y - h)
        for w in range(x - (wid - diff), x + (wid - diff) + 1):
            if 0 <= h <= R - 1 and 0 <= w <= C - 1:
                dp[h][w] = "x"
# "x"がついたところ起点で菱形状に"X"をつける（候補から除外する）
for i in range(R):
    for j in range(C):
        if S[i][j] == "x":
            diam(j, i, K, Salta)

cnt = 0
# はじの方はやるまでもなくX
for i in range(wid, R - wid):
    for j in range(wid, C - wid):
        if Salta[i][j] == "o":
            cnt += 1
print(cnt)
