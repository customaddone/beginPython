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

    # これ追加
    def count_group(self):
        return len({self.find(x) for x in range(n)})

N = 100
K = 7
query = [
[1, 101, 1],
[2, 1, 2],
[2, 2, 3],
[2, 3, 3],
[1, 1, 3],
[2, 3, 1],
[1, 5, 5]
]

U = UnionFind(3 * N)

def checker(int_input, x, y):
    if x < 0 or x >= N or y <0 or y >= N or int_input < 1 or int_input > 2:
        return False
    else:
        return True

for i in query:
    int_input = i[0]
    x = i[1]
    y = i[2]

    if not checker(int_input, x, y):
        print(int_input, x, y)
        continue

    if int_input == 1:
        # xとyが異種の場合
        if U.same(x, y + N) or U.same(x, y + 2 * N):
            print(int_input, x, y)
            continue
        else:
            # x == A and y == A
            U.union(x, y)
            # x == B and y == B
            U.union(x + N, y + N)
            U.union(x + 2 * N, y + 2 * N)

    if int_input == 2:
        # x,y が同種、もしくは逆の場合
        if U.same(x, y) or U.same(x, y + 2 * N):
            print(int_input, x, y)
            continue
        else:
            U.union(x, y + N)
            U.union(x + N, y + 2 * N)
            U.union(x + 2 * N, y)
