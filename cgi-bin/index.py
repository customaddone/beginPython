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

N = input()
K = getN()
L = len(N)

dp = [[[0] * 4 for i in range(2)] for i in range(L + 1)]
# i桁目がdで個数がkのとき
dp[0][0][0] = 1

for i in range(L):
    # 各桁について
    D = int(N[i])

    # N = 103のとき
    # j == 0 103
    # j == 1 0 ~ 102まで
    for j in range(2):
        #
        for d in range(10 if j else D + 1):
            for k in range(4):
                # d == 0のときkのカウントは進まない
                if d == 0:
                    # j == 1なら何も起こらない
                    # j == 0でd == Dのときのみj == 0の列を +
                    dp[i + 1][j | (d < D)][k] += dp[i][j][k]
                else:
                    if k + 1 <= 3:
                        dp[i + 1][j | (d < D)][k + 1] += dp[i][j][k]

print(dp[L][0][K] + dp[L][1][K])



#
