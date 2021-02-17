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

# その時点での最小値を求めてくれる　嬉しい

class Multiset:
    def __init__(self):
        self.h = []
        self.d = dict()

    def insert(self,x):
        heappush(self.h,x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self,x):
        if x not in self.d or self.d[x] == 0:
            return 'not found'
        else:
            self.d[x] -= 1

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heappop(self.h)
            else:
                break

    def erase_all(self,x):
        if x not in self.d or self.d[x] == 0:
            return 'not found'
        else:
            self.d[x] = 0

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self):
        if len(self.h) == 0:
            return 'enpty'
        return self.h[0]

# ABC170 smart infant

N, Q = getNM()
limit = 2 * (10 ** 5) + 1

infants = [getList() for i in range(N)]
trans = [getList() for i in range(Q)]
belong = [0] * N
rate = [0] * N

school = [Multiset() for i in range(limit)]
purity = Multiset()

# 各学校にいる生徒を記録する
for i in range(N):
    a, b = infants[i]
    b -= 1
    belong[i] = b
    rate[i] = -a
    school[b].insert(-a)

# 各学校の最強園児を求める
for i in range(limit):
    if len(school[i].d) > 0:
        purity.insert(-school[i].get_min())

# 転園させる
for c, d in trans:
    c -= 1
    d -= 1
    ### 転園前処理 ###
    prev = belong[c] # 所属変更
    purity.erase(-1 * school[prev].get_min()) # 最強リストから削除
    school[prev].erase(rate[c]) # 前の学校から削除
    if len(school[prev].h) > 0:
        purity.insert(-1 * school[prev].get_min()) # 最強リストを更新
    ################

    ### 転園後処理 ###
    belong[c] = d
    after = belong[c] # 所属変更
    if len(school[after].h) > 0:
        purity.erase(-1 * school[after].get_min()) # 最強リストから削除
    school[after].insert(rate[c]) # 次の学校に追加
    purity.insert(-1 * school[after].get_min()) # 最強リストを更新
    #################

    print(purity.get_min())
