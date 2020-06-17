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
N = input()
l = len(N)

# dp[i][0 or 1][j]
# 1つ目の引数　何桁目か
# 2つ目の引数 inputした数になる可能性があるか
# 3つ目の引数　これまで1が何個出てきたか
dp = [[[0] * (l + 1) for _ in range(2)] for _ in range(l + 1)]
dp[0][0][0] = 1

# 例 345
for i in range(l):
    # i = 0の時 v = 3
    # i = 1の時 v = 4

    # i = 0のループ終了時点で
    # dp[1][0][0] = 1 (3○○)
    # dp[1][1][0] = 2 (0○○, 2○○)
    # dp[1][1][1] = 1 (1○○)
    v = int(N[i])

    for j in range(l):
        # 1→1
        # 0○○ + 2○○について02○ ~ 09○まで、22○ ~ 29○まで次のdpを更新（1のカウントは増えす0のまま）
        # 1○○について12○ ~ 19○まで（1のカウントは増えす1のまま）
        dp[i + 1][1][j] += dp[i][1][j] * 9
        # 0○○ + 2○○について01○、21○（1のカウントが1増える）
        # 1○○について11○（1のカウントが1増える）
        dp[i + 1][1][j + 1] += dp[i][1][j]

        # 0→1
        # i = 1のときv = 4なので
        if v > 1:
            # 3○○について32○ ~ 33○まで（1のカウントは増えす0のまま）
            dp[i + 1][1][j] += dp[i][0][j] * (v - 1)
            # 3○○について31○（1のカウントが1増える）
            dp[i + 1][1][j + 1] += dp[i][0][j]
        elif v == 1:
            dp[i + 1][1][j] += dp[i][0][j]

        # 0→0
        if v == 1:
            # 3○○について34○
            dp[i + 1][0][j + 1] = dp[i][0][j]
        else:
            dp[i + 1][0][j] = dp[i][0][j]

ans = 0
for j in range(l + 1):
    # dp[l]について各j(1のカウント)の通りの数 * j
    ans += (dp[l][0][j] + dp[l][1][j]) * j
print(ans)
