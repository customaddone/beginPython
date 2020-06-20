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

N = 5
#es = [[1,2,3],[0,2],[0,1],[0,4],[3]] # False
dist = [
[1, 3],
[0, 2],
[1, 3],
[0, 2, 4],
[3]
] # True

#n個の頂点の色を初期化。0:未着色、1:黒、-1:白
colors = [0] * N

#頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse
def dfs(v, color):
    #今いる点を着色
    colors[v] = color
    #今の頂点から行けるところをチェック
    for to in dist[v]:
        #同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        #未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    #調べ終わったら矛盾がないのでTrue
    return True

#2部グラフならTrue, そうでなければFalse
def is_bipartite():
    return dfs(0,1) # 頂点0を黒(1)で塗ってDFS開始

print(is_bipartite())
