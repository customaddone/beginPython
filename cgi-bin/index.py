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

N, M = 6, 8
query = [
[1, 2],
[2, 3],
[3, 4],
[4, 5],
[5, 1],
[1, 4],
[1, 5],
[4, 6],
]
S, T = 1, 6

def build_tree_dis(N, edge_list):

    G = [[] for i in range(N)]

    for i in range(len(edge_list)):
        a, b = edge_list[i]
        G[a - 1].append(b - 1)

    # 葉（末端の数）
    leaves = []
    for i in range(N):
        if len(G[i]) == 1:
            leaves.append(i)

    return G

edges = build_tree_dis(N, query)

ignore = [[-1] * 3 for i in range(N)]
ignore[S - 1][0] = 0

pos = deque([[S - 1, 0]])

while len(pos) > 0:
    u, t = pos.popleft()
    t += 1
    j = t % 3
    for i in edges[u]:
        if ignore[i][j] == -1:
            ignore[i][j] = t
            pos.append([i, t])

if ignore[T - 1][0] % 3 == 0:
    print(ignore[T - 1][0] // 3)
    exit()
else:
    print(-1)
