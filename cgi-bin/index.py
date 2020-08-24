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

class Reroot():
    def __init__(self, n, query):
        self.n = n
        graph = [[] for i in range(self.n)]
        for x, y in query:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        self.graph = graph
        # トポソ
        P = [-1] * self.n
        Q = deque([0])
        R = []
        while Q:
            i = deque.popleft(Q)
            R.append(i)
            for a in self.graph[i]:
                if a != P[i]:
                    P[a] = i
                    self.graph[a].remove(i)
                    deque.append(Q, a)

        ##### Settings #####
        self.unit = 0
        self.merge = lambda a, b: max(a, b)
        self.adj_bu = lambda a, i: a + 1
        self.adj_td = lambda a, i, p: a + 1
        self.adj_fin = lambda a, i: a
        ####################

        ME = [self.unit] * self.n
        XX = [0] * self.n
        for i in R[1:][::-1]:
            XX[i] = self.adj_bu(ME[i], i)
            p = P[i]
            ME[p] = self.merge(ME[p], XX[i])
        XX[R[0]] = self.adj_fin(ME[R[0]], R[0])

        TD = [self.unit] * self.n
        for i in R:
            ac = TD[i]
            for j in self.graph[i]:
                TD[j] = ac
                ac = self.merge(ac, XX[j])
            ac = self.unit
            for j in self.graph[i][::-1]:
                TD[j] = self.adj_td(self.merge(TD[j], ac), j, i)
                ac = self.merge(ac, XX[j])
                XX[j] = self.adj_fin(self.merge(ME[j], TD[j]), j)

        self.res = XX

N = getN()
que = [getList() for i in range(N - 1)]
tree = Reroot(N, que)
# 最後に最長経路に潜りこむ(行きのみ)
# それ以外の経路については行き帰り2回通るので
# 答えは2(N - 1) - d
for i in tree.res:
    print(2 * (N - 1) - i)
