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

def build_tree(N, edge_list):

    G = [[] for i in range(N)]

    for i in range(len(edge_list)):
        a, b = edge_list[i]
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    # 葉（末端の数）
    leaves = []
    for i in range(N):
        if len(G[i]) == 1:
            leaves.append(i)

    return G, leaves

N = getN()
query = [[] for i in range(N - 1)]
for i in range(N - 1):
    query[i] = getList()

d = list(sorted(getList()))

edges, leaves = build_tree(N, query)

v = leaves[0]

# 最も理想的な場合のsum = d[0] + d[1] + ... + d[-2]
ans = -d[-1]
nodes = [0] * N

# 葉の先端から辿っていく
def dfs(now):
    global ans
    if nodes[now] > 0:
        return
    nodes[now] = d.pop()
    ans += nodes[now]
    for i in edges[now]:
        if nodes[i] > 0:
            continue
        dfs(i)

dfs(v)
print(ans)
print(*nodes)
