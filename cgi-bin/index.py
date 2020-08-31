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

# 根0~iまで通るとj桁目のフラグが偶数本/奇数本集まるか
def search_bit(bit):
     # 木をKから順にたどる（戻るの禁止）
    ignore = [-1] * N
    ignore[0] = 0
    pos = deque([0])

    while len(pos) > 0:
        u = pos.popleft()
        for i in edges[u]:
            if ignore[i[0]] == -1:
                if i[1] & (1 << bit):
                    ignore[i[0]] = ignore[u] + 1
                else:
                    ignore[i[0]] = ignore[u]
                pos.append(i[0])
    # 欲しい情報は偶数本/奇数本集まるかのみ
    ignore = [i % 2 for i in ignore]
    return ignore

flags = []
for i in range(31):
    flags.append(search_bit(i))

# flagsの情報を基に0~i間のXor(31桁bit換算)を求める
# aとbの共通祖先をkとすると
# a ^ b =
# 0 ~ k ~ a ^ 0 ~ k ~ b = 0 ~ a ^ 0 ~ b
# (0 ~ k ^ 0 ~ k)が0なので
dis = [''] * N
for i in range(N):
    opt = ''
    for j in range(30, -1, -1):
        if flags[j][i] == 0:
            opt += '0'
        else:
            opt += '1'
    dis[i] = opt

# （1についてTrue, 2についてFalse...みたいなのは
# bit換算してdictに収納できる）
dict = defaultdict(int)
for i in range(N):
    dict[dis[i]] += 1

ans = 0
for bit in dis:
    #　bit ^ opt = Xとなるoptが欲しい =
    # opt = bit ^ X
    opt = int(bit, 2) ^ X
    s = ''
    for j in range(30, -1, -1):
        if opt & (1 << j):
            s += '1'
        else:
            s += '0'
    # a ^ a = 0になるので
    if X == 0:
        ans += dict[s] - 1 # 自身を引く
    else:
        ans += dict[s]
print(ans // 2) # a ~ bとb ~ a２回足されるので
