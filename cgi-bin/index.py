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
from math import sqrt
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

W, H, N = 10, 10, 5
# (x1, y1)から(x2, y2)まで線を引く
X1 = [i - 1 for i in [1, 1, 4, 9, 10]]
X2 = [i - 1 for i in [6, 10, 4, 9, 10]]
Y1 = [i - 1 for i in [4, 8, 1, 1, 6]]
Y2 = [i - 1 for i in [4, 8, 10, 5, 10]]

# 縦
row = set()
r_index = {}
# 横
col = set()
c_index = {}
# 変換
for x, y in zip(X1 + X2, Y1 + Y2):
    # どの横列が必要か
    row.add(y)
    if y > 0:
        row.add(y - 1)
    if y < H:
        row.add(y + 1)

    # どの縦列が必要か
    col.add(x)
    if x > 0:
        col.add(x - 1)
    if x < W:
        col.add(x + 1)

# 圧縮後のどの座標になるか
row = sorted(list(row))
for i in range(len(row)):
    r_index[row[i]] = i

col = sorted(list(col))
for i in range(len(col)):
    c_index[col[i]] = i

X1 = [c_index[i] for i in X1]
X2 = [c_index[i] for i in X2]
Y1 = [r_index[i] for i in Y1]
Y2 = [r_index[i] for i in Y2]

#  以下省略
dp = [[0] * len(col) for i in range(len(row))]
