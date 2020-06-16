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

N, M = getNM()
dp = [float("inf")] * (1 << N)
dp[0] = 0

# 1 ~ Nを全て開けられる鍵を揃えるコストの最小値がO(M * 2 ** N)でわかる
# 各鍵について
for i in range(M):
    a, b = getNM()
    c = getList()
    bit = 0
    # その鍵で開けられる部屋を揃える
    for item in c:
        bit |= (1 << (item - 1))
    # 部屋の各状態について
    # そこからさらに鍵cを取得した場合と他の鍵を使用した場合とで比較する
    for j in range(1 << N):
        dp[j | bit] = min(dp[j | bit], dp[j] + a)

if dp[(1 << N) - 1] == float("inf"):
    print(-1)
else:
    print(dp[(1 << N) - 1])
