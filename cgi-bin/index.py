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

N = getN()
# 座標xにあり、半径r
# ri - (xi - xi-1) - ri-1 > 0ならCi-1はCiの内部に含まれる
# ri + xi-1 > ri-1 + xiなら
circle = []
for i in range(N):
    x, r = getNM()
    circle.append([x - r, x + r]) # 端点のみ抑える

# N <= 10 ** 5なので最大流無理
# 貪欲?

# もしleftが同じならrightが小さい順に（小→大へ更新していく）
### 今回は最小部分減少を求めるため小さい順に並べる ###
circle.sort(key = lambda i: i[1])
# lが小さい順に並ぶ
circle.sort(key = lambda i: i[0])

# うまく並び変えたあと右端の点のみ取りLIS
### 今回は最小部分減少を求めるため-circle[i][1]を並べる ###
r_list = []
for i in range(N):
    r_list.append(-circle[i][1])

def lis(A):
    L = [A[0]]
    for a in A[1:]:
        # Lの末尾よりaが大きければ増加部分を拡張できる
        if a > L[-1]:
            # 前から順にLに追加していく
            L.append(a)
        else:
            L[bisect_left(L, a)] = a

    # Lの配列の長さは求まる
    # Lの中身はデタラメ
    return len(L)
print(lis(r_list))
