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
mod = 998244353

#############
# Main Code #
#############

# CODE FESTIVAL 2016 Final D. Pair Cards

"""
個数の最大値を求める
ペア

最も条件がきついものからペアにしていく
条件　どちらか
同じ整数
Mの倍数になる

Mが奇数の場合と偶数の場合
奇数の場合
mod mが
0: 自身と
i: m - iと
偶数の場合
0, m // 2: 自身と
i: m - iと

効率のいい組み合わせ
きつい順から
min(len(i), len(m - i))になるが差分については同じ数同士をペアにできる

同じ数がグループにある数はその同じ数と結ぶことができるし、m - iのグループの数と結ぶことも
できる　条件は緩い
そうではない条件が厳しいものを優先して結ぶ
"""

N, M = getNM()
X = getList()

modulo = [[] for i in range(M)]
for x in X:
    modulo[x % M].append(x)

ans = (len(modulo[0]) // 2) + (len(modulo[M // 2]) // 2) * (M % 2 == 0)
half = M // 2 if M % 2 == 0 else (M // 2) + 1

for i in range(1, half):
    pair1 = 0
    dict1 = defaultdict(int)
    for j in modulo[i]: # 同じ数
        if dict1[j] == 1:
            dict1[j] -= 1
            pair1 += 1
        else:
            dict1[j] += 1

    pair2 = 0
    dict2 = defaultdict(int)
    for j in modulo[M - i]:
        if dict2[j] == 1:
            dict2[j] -= 1
            pair2 += 1
        else:
            dict2[j] += 1

    if len(modulo[i]) > len(modulo[M - i]): # pair1を使う
        ans += len(modulo[M - i])
        diff = abs(len(modulo[i]) - len(modulo[M - i])) // 2
        ans += min(diff, pair1)
    else:
        ans += len(modulo[i])
        diff = abs(len(modulo[i]) - len(modulo[M - i])) // 2
        ans += min(diff, pair2)

print(ans)
