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

H, W, K = getNM()

if W == 1:
    print(1)
    exit()

# 左からi本目の右、左に橋がかかっている通り、両方に通ってない通り
bridge_right = [0] * W
bridge_left = [0] * W
not_bridge = [0] * W

for bit in range(1 << (W - 1)):
    flag = True
    for i in range(1, (W - 1)):
        if bit & (1 << i) and bit & (1 << (i - 1)):
            flag = False
    if flag:
        for i in range(W):
            if i == 0:
                if bit & (1 << i):
                    bridge_right[i] += 1
                else:
                    not_bridge[i] += 1
            elif i == W - 1:
                if bit & (1 << (i - 1)):
                    bridge_left[i] += 1
                else:
                    not_bridge[i] += 1
            else:
                if bit & (1 << i):
                    bridge_right[i] += 1
                elif bit & (1 << (i - 1)):
                    bridge_left[i] += 1
                else:
                    not_bridge[i] += 1

dp = [[0] * W for i in range(H + 1)]

dp[0][0] = 1
for i in range(1, W):
    dp[0][i] = 0

# まっすぐ降りて来た場合、右から降りてきた場合、左から降りてきた場合
for i in range(1, H + 1):
    for j in range(W):
        dp[i][j] += dp[i - 1][j] * not_bridge[j]
        if j == 0:
            dp[i][j + 1] += dp[i - 1][j] * bridge_right[j]
        elif j == W - 1:
            dp[i][j - 1] += dp[i - 1][j] * bridge_left[j]
        else:
            dp[i][j + 1] += dp[i - 1][j] * bridge_right[j]
            dp[i][j - 1] += dp[i - 1][j] * bridge_left[j]

print(dp[-1][K - 1] % mod)
