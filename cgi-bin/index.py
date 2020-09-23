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

# dfs部分和問題
def dfs(i, sum):
    if i == N:
        return sum == K
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + A[i]):
        return True
    return False

N, K = map(int, input().split())
A = list(map(int, input().split()))

if dfs(0, 0):
    print("Yes")
else:
    print("No")

# dfsナップサック
def rec_memo(i, j):
    if dp[i][j]:
        return dp[i][j]
    if i == N:
        res = 0
    elif j < w[i]:
        res = rec_memo(i + 1, j)
    else:
        res = max(rec_memo(i + 1, j), rec_memo(i + 1, j - w[i]) + v[i])
    dp[i][j] = res
    return res

N = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]

W = 5
dp = [[0] * (W + 1) for i in range(N + 1)]  # メモ化テーブル
print(rec_memo(0, W))

# 個数制限あり（３個）重複なし再帰
N, X = getNM()
lista = [i for i in range(1, N + 1)]
dp = [[0] * (N + 1) for i in range(N)]
ans = 0

def rec_memo(i, plus, sum):
    global ans
    if i == N or plus == 3:
        if plus == 3:
            print([i, sum])
            ans += (sum == 0)
    elif sum < lista[i]:
        rec_memo(i + 1, plus, sum)
    else:
        rec_memo(i + 1, plus, sum)
        rec_memo(i + 1, plus + 1, sum - lista[i])
rec_memo(0, 0, X)

# 個数制限なし重複あり再帰部分和
# 1 + 3 と3 + 1 と1 + 1 + 1 + 1は違う通りになる
# dfs使った方がいい
def dfs(now, sum):
    if sum <= 0:
        return sum == 0
    res = 0
    for i in range(now, W):
        res += dfs(i, sum - a[i])
    return res

a = [1, 3, 5, 7, 9]
W = len(a)
A = 9
print(dfs(0, A))
