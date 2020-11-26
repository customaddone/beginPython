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

# 高速版半分全列挙

"""
Nちいさ　半分全列挙すらできる
ナップサックでいいじゃ
枝借りする
relistの部分

ソートがなければ
266356045
273062972
262630505
265065557
269337432
271772484
273555143
262605352
"""

N, T = getNM()
A = getList()

# O(2 ** N // 2)でできるんじゃ
def relist(array):
    o1 = []
    o2 = []
    for i in range(len(array)):
        if i == 0:
            o1.append(0)
            o1.append(array[0])
            continue

        for j in range(len(o1)):
            o2.append(o1[j] + array[i])
        alta = deque([])

        while o1 or o2:
            if not o1:
                while o2:
                    alta.appendleft(o2.pop())
                break
            elif not o2:
                while o1:
                    alta.appendleft(o1.pop())
                break
            u1 = o1.pop()
            u2 = o2.pop()
            if u1 >= u2:
                alta.appendleft(u1)
                o2.append(u2)
            else:
                alta.appendleft(u2)
                o1.append(u1)
        o1 = list(alta)

    return o1

B = relist(A[:N // 2])
F = relist(A[N // 2:]) # こっちの方が大きい

if not B:
    ans = 0
    for f in F:
        if f <= T:
            ans = max(ans, f)
    print(ans)
    exit()

# 尺取り法でO(2 ** N // 2)でできるんじゃ
ans = 0
r = len(B) - 1
for f in F:
    while r > 0 and f + B[r] > T:
        r -= 1
    opt = f + B[r]
    if opt <= T:
        ans = max(ans, opt)

print(ans)

# ARC073 D - Simple Knapsack

# あらかじめw1で引いておいたらいい気がする
N, W = getNM()
WV = [getList() for i in range(N)]
d = defaultdict(int)
d[0] = 0 # dictで持つ

for i in range(N):
    w, v = WV[i]
    all = list(d.items()) # アイテム解放
    for w_s, v_s in all:
        if w_s + w <= W:
            # w1近辺, w1 * 2近辺, w1 * 3近辺...に集まるので
            # サイズはそんなに大きくならない
            d[w_s + w] = max(d[w_s + w], v_s + v)

print(max(d.values()))
