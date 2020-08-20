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
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

# ABC149 E - Handshake
N, K = 9, 14
A = [1, 3, 5, 110, 24, 21, 34, 5, 3]

A.sort(reverse = True)

# 各ペアを大きい順に並べるのはムリ
# ただし、合計がx以上/以下になるペアが何個あるかは求められる
# x以上になるペアが何個あるか
def cnt(x):
    r = 0
    ans = 0
    list_num = [0] * N
    for i in range(N - 1, -1, -1):
        while r < N and A[r] + A[i] >= x:
            r += 1
        list_num[i] = r
        ans += r

    return [ans, list_num]

ng = 0
ok = 2 * (10 ** 6)

while ok - ng > 1:
    mid = (ok + ng) // 2
    if cnt(mid)[0] <= K:
        ok = mid
    else:
        ng = mid

# 境界がわかったら
imos = [0] + copy.deepcopy(A)
for i in range(N):
    imos[i + 1] += imos[i]

ans = 0
plus = cnt(ok)[1]

# cntから得た情報を元に上から順番に足していく
for i in range(N):
    ans += (A[i] * plus[i]) + imos[plus[i]]
# 合計がngになるペアを足りない分K - sum(plus)個足す
ans += ng * (K - sum(plus))
print(ans)

# ABC155 D - Pairs
N, K = 10, 40
A = [5, 4, 3, 2, -1, 0, 0, 0, 0, 0]
minus = [-x for x in A if x < 0]
plus = [x for x in A if x >= 0]

minus.sort()
plus.sort()

def cnt(x):
    ans = 0
    if x < 0:
        x = -x
        r = 0
        # - * +
        for num in minus[::-1]:
            while r < len(plus) and plus[r] * num < x:
                r += 1
            ans += len(plus) - r
        return ans

    r = 0
    for num in minus[::-1]:
        if num * num <= x:
            ans -= 1
        while r < len(minus) and minus[r] * num <= x:
            r += 1
        ans += r
    r = 0
    for num in plus[::-1]:
        if num * num <= x:
            ans -= 1
        while r < len(plus) and plus[r] * num <= x:
            r += 1
        ans += r
    ans //= 2
    # -になるものはまとめて計算
    ans += len(minus) * len(plus)
    return ans

bottom = 0
top = 2 * (10 ** 18) + 2


while top - bottom > 1:
    mid = (top + bottom) // 2
    if cnt(mid - 10 ** 18 - 1) < K:
        bottom = mid
    else:
        top = mid

print(int(top - 10 ** 18 - 1))
