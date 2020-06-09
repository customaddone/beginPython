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

# ガソスタの個数
N = 4
#　距離
L = 25
# 最初の燃料
P = 10
# ガソスタの位置
A = [10, 14, 20, 21]
# ガソスタの補給量
B = [10, 5, 2, 4]

gas = []
heapq.heapify(gas)

tank = P
now = 0
ans = 0

for i in range(N):
    # 一旦ガソリンスタンドまで進む予定に
    dis = A[i] - now
    # タンクが貯まるまで続ける
    while (tank - dis) < 0:
        if len(gas) == 0:
            print(-1)
            exit()
        tank += heapq.heappop(gas)
        ans += 1
        
    tank -= dis
    now = A[i]
    heapq.heappush(gas, B[i])
print(ans)
