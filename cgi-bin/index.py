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
mod = 998244353
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# パ研合宿2020　第1日「SpeedRun」
# 同じgcdを持つ区間は結合しても同じまま

"""
K個に切り分ける
それぞれの部分の総和のgcdが大きいほどいい
最大公約数はいくつになるか
二分探索したいが dpもしたい

300C150とかは無理

K = 1から考える
答えはAの総和

A が最大300しかない
エッジを貼る
k回辺を移動して0 ~ Nにいけるか

調和級数
"""

N = getN()
A = [0] + getList()
su = sum(A)
for i in range(1, N + 1):
    A[i] += A[i - 1]

ans = [0] * (N + 1)
for i in range(su + 1, 0, -1):
    # これを通過すると必ず条件を満たす区間を作れる
    if su % i != 0:
        continue

    cnt = 0
    last = 0
    for j in range(1, N + 1):
        if (A[j] - A[last]) % i == 0:
            last = j
            cnt += 1

    # cnt以下の区間は結合することで簡単に作れる
    for a in range(cnt + 1):
        ans[a] = max(ans[a], i)

for a in ans[1:]:
    print(a)
