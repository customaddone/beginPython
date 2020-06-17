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

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

N = 10

query = [
[4, 8, 6831],
[1, 8, 4583],
[0, 5, 6592],
[0, 6, 3063],
[3, 8, 4975],
[1, 8, 2049],
[4, 7, 2104],
[2, 7, 781]
]

U = UnionFind(N)

for i in query:
    U.union(i[0], i[1])

def part_spanning(members, query):
    mem_alta = [-1] * (members[-1] + 1)
    N_a = len(members)
    for i in range(N_a):
        mem_alta[members[i]] = i

    part_query = []
    for i in query:
        if i[0] in members or i[1] in members:
            part_query.append(i)
    # 今回大きい順に繋いだ
    part_query.sort(reverse = True, key = lambda i:i[2])

    U1 = UnionFind(N_a)
    res = 0
    for e in part_query:
        a, b, cost = e
        # members.index(a)だと計算量が多くなる
        if not U1.same(mem_alta[a], mem_alta[b]):
            res += cost
            U1.union(mem_alta[a], mem_alta[b])
    return res

# 各グループごとに最小全域木
ans = 0
for i in U.all_group_members().values():
    ans += (len(i) * 10000 - part_spanning(i, query))
print(ans)
