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

# indeedなう　D - 高橋くんと数列

"""
その数を一つでも含む連続部分列を返す
各iにつきO(1)で
含まないものを引こう
"""

N, C = getNM()
A = getList()

# 数字A[i]の最後の場所
p = [-1] * (C + 1)
ans = [0] * (C + 1)

for i in range(N):
    # 片方で前回以降の分だけ、片方で最後まで
    # lを固定してrをl+1 ~ Nにすればダブらない
    # さらに前回の場所 + 1 ~ をlにもできる
    ans[A[i]] += (i - p[A[i]]) * (N - i)
    p[A[i]] = i

for i in ans[1:]:
    print(i)

# ARC045 B - ドキドキデート大作戦高橋君

"""
NlogNを目指す
i番目の区間をサボってもいい
= l ~ rの全区間で二重以上に清掃がされていること
"""

N, M = getNM()
clean = [getList() for i in range(M)]

# 累積
room = [0] * (3 * 10 ** 5 + 7)
for s, t in clean:
    room[s] += 1
    room[t + 1] -= 1

forbit = []
for i in range(3 * 10 ** 5 + 7):
    room[i] += room[i - 1]
    if room[i] <= 1:
        forbit.append(i)

# 判定
ans = []
for i in range(M):
    s, t = clean[i]
    # sがforbit内の数と同じ数字を踏むと反対方向に飛ぶように
    if bisect_left(forbit, s) == bisect_right(forbit, t):
        ans.append(i + 1)

print(len(ans))
for i in ans:
    print(i)
