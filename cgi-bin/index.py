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

N, X = getNM()
edge_list = [getList() for i in range(N - 1)]

def build_tree_dis(n, edge_list):

    G = [[] for i in range(n)]

    for a, b, c in edge_list:
        G[a - 1].append([b - 1, c])
        G[b - 1].append([a - 1, c])

    return G

edges = build_tree_dis(N, edge_list)

dict = defaultdict(int)
dict[0] = 1
# 各地点ごとで数えあげる
# a ~ bがペアで、bの方がaより探索が遅い
# a探索時 ans増えない
# b探索時 ans増える
# のでダブらない
ans = 0

def search_bit():
    global ans
     # 木をKから順にたどる（戻るの禁止）
    ignore = [-1] * N
    ignore[0] = 0
    pos = deque([0])

    while len(pos) > 0:
        u = pos.popleft()
        for i in edges[u]:
            if ignore[i[0]] == -1:
                rec = ignore[u] ^ i[1]
                ignore[i[0]] = rec
                ans += dict[rec ^ X] # ansに加算 自身をペアにするのを防ぐためにレコードの前に行う
                dict[rec] += 1 # レコード
                pos.append(i[0])

search_bit()
print(ans)
