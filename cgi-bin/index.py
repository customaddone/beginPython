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
que = [getList() for i in range(N)]
# 正直にやればN!

# dpか二分探索か
# dpだと各dp[i]:iまで進んだにどの要素を使った/使ってないかの情報が必要
# ok, ng型二分探索　どっちみち貪欲に行った場合どのような値をとるかが必要

# 貪欲法　最も効率の良い並べ方は何か

# 上がって下がることを考えず、上がるだけ、下がるだけの場合は？
# まず下がるものだけを並べ、次に上がるものを並べる（谷の形にすればいい）
# 下がるもの内の並べ方は？　自由でいい

# 今回の問題だと下がるもの内の並べ方も考える必要がありそう
# → 上がり幅が大きいものは出来るだけ谷の底に沈めたい

plus = []
minus = []
for i in que:
    if i[0] - i[1] >= 0:
        plus.append(i)
    else:
        minus.append(i)
plus.sort(reverse = True, key = lambda i:i[1])
minus.sort()

now = 0
res = -float('inf')
for i in minus:
    res = max(res, now + i[0])
    now += i[0] - i[1]

for i in plus:
    res = max(res, now + i[0])
    now += i[0] - i[1]
print(res)
