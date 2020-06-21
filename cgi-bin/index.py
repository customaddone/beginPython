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
mod = 998244353


#############
# Main Code #
#############

# N:ブロック
# M:色（バリエーション）
# K:隣合う組み
# N, M, K = 6, 2, 3のとき
# K = 0 のとき
# 121212, 212121
# K = 1のとき,
# 12121 のどこかに同じ数字を挟み込めば
# 112121, 122121という風にできる
# K = 2のとき
# 1212 のどこかに同じ数字を挟む　を２回行う
# 112212, 112122もできるし
# 111212, 122212もできる
N, M, K = getNM()

# 重複組み合わせのため
# 繰り返し使うのでこのタイプ
Y = N + K + 1
fact =[1] #階乗
for i in range(1, Y + 1):
    fact.append(fact[i - 1] * i % mod)

facv = [0] * (Y + 1) #階乗の逆元
facv[-1] = pow(fact[-1], mod - 2 , mod)

for i in range(Y - 1, -1, -1):
    facv[i] = facv[i + 1] * (i + 1) % mod

def cmb(n, r):
    if n < r:
        return 0
    return fact[n] * facv[r] * facv[n - r] % mod

ans = 0
for i in range(K + 1):
    opt = M * pow(M - 1, N - i - 1, mod) * cmb(N - i + i - 1, i)
    ans += opt % mod
print(ans % mod)
