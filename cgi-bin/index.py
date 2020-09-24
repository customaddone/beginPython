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

# ABC023 C - 収集王
# 経路圧縮

R, C, K = getNM()
N = getN()
query = [getList() for i in range(N)]

# 縦hに行くとi個飴がもらえる
h_list = defaultdict(int)
w_list = defaultdict(int)
h_len = set()
w_len = set()

for h, w in query:
    h -= 1
    w -= 1
    h_list[h] += 1
    w_list[w] += 1
    h_len.add(h)
    w_len.add(w)

# 飴がj個もらえる行はどこか
candy_h = defaultdict(list)
candy_w = defaultdict(list)

for i in h_list.items():
    candy_h[i[1]].append(i[0])
for i in w_list.items():
    candy_w[i[1]].append(i[0])

# 縦のキャンディの個数が1 ~ K - 1の行それぞれについて
# 横のキャンディの個数がK - 1 ~ 1の列を調べて掛け合わせ
cnt = 0
for i in candy_h.items():
    if K - i[0] >= 1:
        cnt += len(i[1]) * len(candy_w[K - i[0]])

# 縦が0個
cnt += (R - len(h_len)) * len(candy_w[K])
# 縦がN個
cnt += (C - len(w_len)) * len(candy_h[K])

# 足しすぎたもの、足していないものを修正
for r, c in query:
    r -= 1
    c -= 1
    if h_list[r] + w_list[c] == K:
        cnt -= 1
    elif h_list[r] + w_list[c] == K + 1:
        cnt += 1

print(cnt)
