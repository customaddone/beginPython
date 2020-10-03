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

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

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
mod = 10 ** 9 + 7


#############
# Main Code #
#############
# 2N階までのタワー
# 部分的にどこで乗ったか、降りたかがわからない
# 同時に乗ってた人について、
# 判定する問題
# 条件は？

N = getN()
que = []
for i in range(N):
    a, b = getNM()
    if (a >= 1 and b >= 1) and b <= a:
        print('No')
        exit()

# 各階について、乗った人 + 降りた人はただ一人
# -1があれば、猶予がある
# 区間で乗り降りした人 = b - a - 1
# これが同時に乗っている人との間で一致すればいい

# 一番簡単なのは1 ~ 3, 2 ~ 4とか
# なんか最大流みたいにならない？

# a ~ b間が大きい場合どうする？
# 間を配分する
# 階数的に 1 ~ 4, 3 ~ 6みたいなのは無理
# 1 ~ 4がいた場合関係するのは2, 3スタートの人

# セグ木かもしれない
