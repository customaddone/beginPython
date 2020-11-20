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

# F - Knapsack for All Segments 
"""
11111 P = 20 の場合

11111 - 11 = 11100
実際には111は20で割れないけど、
[0, 1, 11, 11, 11, 11]
11111を20で割った余りが11
11を20で割った余りが11
11100 = 111 * 100
111は20で割れないけど、100が20で割れるので11100の余りが0になる
100と20の効果を打ち消したい
1[0000] * pw[4]
1[000] * pw[3]
1[00] * pw[2]
1[0] * pw[1]
1 * pw[0]

1 * pw[4 - 2]
1 * pw[3 - 2]
1 * pw[2 - 2] の計算

Pは素数 2とか5の場合もある
それだけ場合分け

4 2
1111 の時　答えは0
右端が偶数かどうか

4 5
1111 の時　答えは0
右端が0か5か
"""

N, P = getNM()
C = input()[::-1]

if P == 2:
    ans = 0
    for i in range(N):
        if int(C[i]) % 2 == 0:
            ans += N - i
    print(ans)

elif P == 5:
    ans = 0
    for i in range(N):
        if int(C[i]) == 0 or int(C[i]) == 5:
            ans += N - i
    print(ans)

else:
    mod = [0]
    pw = 1 # 10 ** iをPで割った時の余り
    for c in C:
        mod.append((int(c) * pw + mod[-1]) % P)
        pw = pw * 10 % P # 10 ** iをPで割った時の余りから10 ** (i + 1)をPで割った時の余りを求める

    print(sum(v * (v - 1) // 2 for v in Counter(mod).values()))
