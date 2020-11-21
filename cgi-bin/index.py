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

"""
N <= 10 ** 15
kを決める
k * (k + 1) // 2がNの倍数になるもののうち、最小のkを求めよ
N = 11の時
合計値11 だめ
合計値22 だめ...
合計値55 10 * 11 // 2 = 55 ok

2 * N * p = k * (k + 1)となるkがあるようなpを求めたい
N = 12 = 2 * 2 * 3の時
p = 1とすると
k候補の2の個数 0個か1個か2個
k候補の2の個数 0個か1個

適当に数字を掛け合わせて隣り合う数字になるものを作りたい
1 と 12
2 と 6
4 と 3
3 と 4
12 と 1
これをp側でもやる

因数分解する　かけ合わせる　間に合わない

int = math.sqrt(2 * N * p)とするとint = kになりうるか
N以下の全ての整数で試すのは無理

22 * p = k * (k + 1)
k * (k + 1) を2 * Nで割れるか
k * (k + 1)は2と(Nの因数)を約数に持つか
隣り合う整数は互いに素なので
奇数と偶数 + 奇数混合に分ける
奇数の因数のうち何個が混合の方に行くか
"""

def CRT(b1, m1, b2, m2):
    def extGcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = extGcd(b % a, a)
        return g, x - (b // a) * y, y

    d, p, q = extGcd(m1, m2)
    if (b2 - b1) % d != 0:
        return 0, -1
    m = m1 * (m2 // d)
    tmp = (b2 - b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return r, m


def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

# CRTする

n = getN()
div = make_divisors(2 * n)
res = float('inf')
for x in div:
    y = 2 * n // x
    k = CRT(0, x, -1, y)
    if k[0] != 0:
        res = min(res, k[0])
print(res)
