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

H, W = 3, 4
# maze = [getList() for i in range(H)]
maze = [
[1, 2, 1, 2],
[2, 3, 2, 3],
[1, 3, 1, 3]
]

# 二次元累積和
dp_sum = [[0] * W for i in range(H)]
dp_1 = [[0] * W for i in range(H)]
dp_2 = [[0] * W for i in range(H)]
dp_3 = [[0] * W for i in range(H)]

# x = 0 ~ i, y = 0 ~ j までの数の合計
def bi_cumul_sum(dp_n):
    # 縦１行目、横１行目
    for i in range(H):
        dp_n[i][0] = maze[i][0]
    for i in range(H):
        for j in range(1, W):
            dp_n[i][j] = dp_n[i][j - 1] + maze[i][j]
    # 全て
    for i in range(1, H):
        for j in range(W):
            dp_n[i][j] += dp_n[i - 1][j]
bi_cumul_sum(dp_sum)
# print(dp_sum)

# x = 0 ~ i, y = 0 ~ j までに出るnumの回数の合計
def bi_cumul_cnt(num, dp_m):
    # 縦１行目、横１行目
    for i in range(H):
        if maze[i][0] == num:
            dp_m[i][0] = 1
    for i in range(H):
        for j in range(1, W):
            if maze[i][j] == num:
                dp_m[i][j] = dp_m[i][j - 1] + 1
            else:
                dp_m[i][j] = dp_m[i][j - 1]
    # 全て
    for i in range(1, H):
        for j in range(W):
            dp_m[i][j] += dp_m[i - 1][j]
bi_cumul_cnt(3, dp_3)
# print(dp_1)

# x = sx ~ ex y = sy ~ eyまで
def judge(sx, sy, ex, ey, dp_l):
    mother = dp_l[ey][ex]
    minus1 = 0
    minus2 = 0
    plus = 0
    if sx > 0:
        minus1 = dp_l[ey][sx - 1]
    if sy > 0:
        minus2 = dp_l[sy - 1][ex]
    if sx > 0 and sy > 0:
        plus = dp_l[sy - 1][sx - 1]
    return mother - minus1 - minus2 + plus

print(judge(1, 1, 3, 2, dp_sum))
print(judge(2, 1, 3, 2, dp_3))
