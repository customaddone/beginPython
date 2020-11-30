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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ABC153 F - Silver Fox vs Monster

# 遅延セグは使わない
# 二分探索したい
# imosする
# どこに爆弾を投下するか
# 効率のいい方法
# 現在地点に爆弾を投下してモンスターを倒すまで
# -D ~ Dまで = 前に2 * Dの範囲に効くと
# bisect_right

N, D, A = getNM()
# 座標Xにいる 体力はH
mons = [getList() for i in range(N)]
mons.sort()
X = []
H = []
for x, h in mons:
    X.append(x)
    H.append(h)

# 累積ダメージ
cnt = 0
r = 0
imos = [0] * (N + 1)
for i in range(N):
    # 爆風範囲
    while r < N and X[i] + 2 * D >= X[r]:
        r += 1
    if i > 0:
        imos[i] += imos[i - 1]
    # ここで爆弾を投下する回数
    hp = max(H[i] - imos[i], 0)
    t = (hp + A - 1) // A # 爆風のぶんを削る
    cnt += t
    # imos
    imos[i] += t * A
    imos[r] -= t * A

print(cnt)
