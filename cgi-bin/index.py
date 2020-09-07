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

# p128 lower_bound
N = 5
A = [2, 3, 3, 5, 6]
K = 3

# K以上であるAiのうち最も左にあるもののインデックス
print(bisect_left(A, K))

# p129 cable master
N = 4
K = 11
L = [8.02, 7.43, 4.57, 5.39]

def f(target):
    cnt = 0
    for i in range(N):
        cnt += math.floor(L[i] / target)
    if cnt >= K:
        return True
    else:
        return False

ng = 0
ok = 10 ** 9 + 1
for i in range(100):
    mid = (ng + ok) / 2
    if f(mid):
        ng = mid
    else:
        ok = mid
print(math.floor(ok * 100) / 100) # 小数点２位まで求める

# p131 aggressive cows
N = 5
M = 3
X = [1, 2, 8, 4, 9]
X.sort()

def c(d):
    last = 0
    # M - 1回indexを進められなかったらFalse
    for _ in range(M - 1):
        crt = last + 1
        while crt < N and X[crt] - X[last] < d:
            crt += 1
        if crt == N:
            return False
        last = crt # indexを進める
    return True

ok = -1
ng = 10 ** 9 + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if c(mid):
        ok = mid
    else:
        ng = mid
print(ok)

# p132 平均最大化
# 平均値を仮定する
N = 3
K = 2
W = [2, 5, 2]
V = [2, 3, 1]

def c2(x, w, v):
    cnt = 0
    items = [v[i] - x * w[i] for i in range(N)]
    items.sort(reverse = True)
    for i in range(K):
        cnt += items[i]
    return cnt >= 0

ok = 0
ng = 10 ** 9 + 1

for i in range(100):
    mid = (ng + ok) / 2
    if c2(mid, W, V):
        ok = mid
    else:
        ng = mid
print(ok)
