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

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    # a - 1の場所にwを追加する
    def add(self, a, w):
        x = a
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    # a未満の数字が何個あるか
    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

    def lowerbound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x + 1

N, Q = getNM()
A = getList()
query = [getList() for i in range(Q)]

# 全部1-indexになるので注意
bit = BIT(N + 1)
for i in range(N):
    # [1, 2, 3, 4, 5]の場合
    # 1番目(0 + 1)に１を
    # 2番目(1 + 1)に２を置く
    bit.add(i + 1, A[i])

for a, b, c in query:
    if a == 0:
        bit.add(b + 1, c)
    else:
        # [1, 2, 3, 4, 5]の[0, 3)について聞きたい時
        # bit.get(0 + 1, 3 + 1)
        print(bit.cum(b + 1, c + 1))
