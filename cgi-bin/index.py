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

def diam(x, y, size, dp):
    max_x = len(dp[0]) - 1
    max_y = len(dp) - 1
    wid = size - 1
    flag = True
    if wid <= x <= max_x - wid and wid <= y <= max_y - wid:
        for h in range(y - wid, y + wid + 1):
            diff = abs(y - h)
            for w in range(x - (wid - diff), x + (wid - diff) + 1):
                if dp[h][w] == 'x':
                    flag = False
                    break
            else:
                continue
            break
    else:
        flag = False
    return flag

cnt = 0
xlist = [[-1] for i in range(R)]
for i in range(R):
    for j in range(C):
        if S[i][j] == "x":
            xlist[i].append(j)
for i in range(R):
    xlist[i].append(C)

optlist = [[] for i in range(R)]
for i in range(R):
    for j in range(C):
        wid = K - 1
        index = bisect_right(xlist[i], j)
        #print(i, j, xlist[i][index - 1], xlist[i][index])
        if j - xlist[i][index - 1] > wid and xlist[i][index] - j > wid:
            optlist[i].append(j)

for i in range(wid, R - wid):
    for j in optlist[i]:
        cnt += diam(j, i, K, S)
print(cnt)
