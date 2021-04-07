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

#############
# Main Code #
#############

S = 'aattccooddeerrrr' # 文字列
s_n = len(S)
K = 'atcoder' # 状態　この場合状態数はk_n = 7
k_n = len(K)

# dp[i][j]: Sのi文字目までで部分文字列(Kのj文字目まで)を取り出せる通りの数
# (文字列の長さ + 1) * (状態の数 + 1)のdpを作る
dp = [[0] * (k_n + 1) for i in range(s_n + 1)]
dp[0][0] = 1

for i in range(s_n):
    for j in range(k_n + 1): # k_n + 1にするの忘れない
        # S[i]を選択しない
        dp[i + 1][j] += dp[i][j]
        # S[i]を選択する
        if j < k_n and S[i] == K[j]:
            dp[i + 1][j + 1] += dp[i][j]

print(dp[s_n][k_n])

# ABC104 D - We Love ABC
S = '????C?????B??????A???????'
N = len(S)

# 状態数はA, AB, ABCの３通り
# dp[i][j]: i番目にjまで丸をつけ終えている通り
dp = [[0] * 4 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    # S[i]を選択しない
    for j in range(4):
        if S[i] != '?':
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
        else:
            dp[i + 1][j] += 3 * dp[i][j]
            dp[i + 1][j] %= mod
    # S[i]を選択する　カウントが進む
    if S[i] == 'A' or S[i] == '?':
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][1] %= mod
    if S[i] == 'B' or S[i] == '?':
        dp[i + 1][2] += dp[i][1]
        dp[i + 1][2] %= mod
    if S[i] == 'C' or S[i] == '?':
        dp[i + 1][3] += dp[i][2]
        dp[i + 1][3] %= mod
        
print(dp[N][3] % mod)
