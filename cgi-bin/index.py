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

# mod不使用ver
def cmb_1(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

# 10
print(cmb_1(5, 3))

# mod使用ver
# nが大きい場合に
def cmb_2(x,y):
    r = 1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * pow(i, mod - 2, mod)) % mod
    return r

# 10
print(cmb_2(5, 3))

# 逆元事前処理ver
# nが小さい場合に
N = 10

fact =[1] #階乗
for i in range(1, N + 1):
    fact.append(fact[i - 1] * i % mod)

facv = [0] * (N + 1) #階乗の逆元
facv[-1] = pow(fact[-1], mod - 2 , mod)

for i in range(N - 1, -1, -1):
    facv[i] = facv[i + 1] * (i + 1) % mod

def cmb(n, r):
    if n < r:
        return 0
    return fact[n] * facv[r] * facv[n - r] % mod
# 120
print(cmb(10, 3))

# 重複組み合わせ
# 10個のものから重複を許して3つとる
print(cmb_1(10 + 3 - 1, 3))

# modが素数じゃない時
def cmb_compose(n, k, mod):
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, k + 1):
            # nCk = n - 1Ck - 1 + n - 1Ck
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod

    return dp[n][k]

print(cmb_compose(10, 3, 50))
