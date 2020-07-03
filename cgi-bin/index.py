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

N, K = getNM()
query = [getList() for i in range(N - 1)]

dist = [[] for i in range(N)]
for a, b in query:
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

fact =[1] #階乗
for i in range(1, K + 1):
    fact.append(fact[i - 1] * i % mod)

facv = [0] * (K + 1) #階乗の逆元
facv[-1] = pow(fact[-1], mod - 2 , mod)

for i in range(K - 1, -1, -1):
    facv[i] = facv[i + 1] * (i + 1) % mod

def cmb(n, r):
    if n < r:
        return 0
    return fact[n] * facv[r] * facv[n - r] % mod

max_root = 0
max_root_index = 0
for i in range(N):
    if len(dist[i]) >= max_root:
        max_root = len(dist[i])
        max_root_index = i

pos = deque([max_root_index])

ans = 1
ignore = [-1] * N
ignore[max_root_index] = 1
ans *= cmb(K, max_root + 1) * math.factorial(max_root + 1)

while len(pos) > 0:
    u = pos.popleft()
    for i in dist[u]:
        if ignore[i] == -1:
            ignore[i] = 1
            if len(dist[i]) >= 2:
                ans *= cmb(K - 2, len(dist[i]) - 1) * math.factorial(len(dist[i]) - 1)
                ans %= mod
            pos.append(i)

print(ans % mod)
