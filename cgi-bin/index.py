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
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

# N日間耐える　初期体力はH
N, H = getNM()
A, B, C, D, E = getNM()

# 普通の食事をn回、質素な食事をm回とり、食事抜きの期間をN - n - m回とした時の
# n, mの値をうまく操って
# An + Cmの最小値を求める
# C < Aなので、制限がなければAn + Cmの最小値は全て質素な食事にした時　
# 最低何回普通の食事nをする必要があるか

# ただし満腹度が0以下になってはいけないので
# H + Bn + Dm - E(N - n - m) >= 1でなければいけない

# 普通の食事の回数n + 質素な食事の回数m(0回からN回まで)を固定してみる
# n + m = k　(0 <= k <= N)
# m = k - n
# H + Bn + D(k - n) - E(N - k)
# H + (B - D)n + Dk - E(N - k) >= 1
# (B - D)n >= 1 - H - Dk + E(N - k)

# numer = 1 - H - Dk + E(N - k)
# denomi = B - D とすると
# n = [numer / denomi]となるnを求める　→ m = k - nなのでmも求まる

ans = float('inf')
for i in range(N + 1):
    n = 0
    m = 0
    # numerがマイナスならどんなn, mでも必ず条件を達成できる
    numer = 1 - H - (D * i) + (E * (N - i))
    denomi = B - D
    if numer <= 0:
        m = i
    else:
        n = (numer + denomi - 1) // denomi
        m = i - n
    if m < 0:
        continue
    ans = min(ans, A * n + C * m)
print(ans)
