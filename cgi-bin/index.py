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
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

N, M = getNM()
A = [int(i) // 2 for i in input().split()]

# 4と8の場合
# 2 6 10 14 18...
# 4 12 20 28... これを２で割ると

# 1 3 5 7 9...
# 2 4 10 14... 起点が偶数と奇数なため永遠に一致しない

# 4と12なら
# 2 6 10 14 18...
# 6 18 30 42... これを２で割ると
# 1 3 5 7 9...
# 3 9 15 21...　になり、起点が奇数と奇数になるためどこかで一致する

# Aの各要素がどれも2でn回ちょうど割れる必要がある
def div_2(n):
    cnt = n
    res = 0
    while cnt > 0:
        if cnt % 2 == 0:
            cnt //= 2
            res += 1
        else:
            return res

def lcm(x, y):
    return x * (y // gcd(x, y))

judge = [div_2(i) for i in A]

if min(judge) != max(judge):
    print(0)
    exit()
L = 1
for i in range(N):
    L = lcm(L, A[i])

# Ai * 0.5, Ai * 1, Ai * 1.5...の個数 - Ai * 1, Ai * 2...の個数
print(M // L - M // (2 * L))
