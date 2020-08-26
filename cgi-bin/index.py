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

"""
N, M = getNM()
weight = []
key = []
for _ in range(M):
    a, b = getNM()
    weight.append(a)
    c = getList()
    key.append(c)

dp = [float('inf')] * (1 << N)
dp[0] = 0
for i in range(M):
    bit = 0
    for item in key[i]:
        bit |= (1 << (item - 1))
    for j in range(1 << N):
        dp[j | bit] = min(dp[j | bit], dp[j] + weight[i])

print(dp)
"""

"""
ARC028 B-特別賞
N, K = getNM()
A = getList()
young = [0] * N
# i番目に若い人の順位はyoung[i]位
for i in range(N):
    young[A[i] - 1] = i

A = [-i for i in A]
# Aの前からK個のリストを作る
prized = []
for i in range(K):
    prized.append(A[i])
heapq.heapify(prized)

# K個数字があるうちの最大値（K番目の数字）を取ってくる
now = heapq.heappop(prized)
print(young[-now - 1] + 1)

for i in range(K, N):
    # もし現在のK番目の数字より小さい数字がきたら
    if A[i] > now:
        # prizedリストに混ぜて（計K個入っている）
        heapq.heappush(prized, A[i])
        # 再びK個数字があるうちの最大値（K番目の数字）を取ってくる
        now = heapq.heappop(prized)
        print(young[-now - 1] + 1)
    # もし現在のK番目の数字より小さい数字がきたら捨てる
    else:
        print(young[-now - 1] + 1)
"""

"""
ABC062 D - 3N Numbers
N = getN()
A = getList()

# 前から計算
fore = A[:N]
# 後ろから計算
back = A[2 * N:]
back = [-i for i in back]
for_sum = sum(fore)
back_sum = sum(back)
heapq.heapify(fore)
heapq.heapify(back)

fore_list = []
back_list = []
for i in range(N):
    fore_list.append(for_sum)
    back_list.append(back_sum)
    in_fore = A[N + i]
    heapq.heappush(fore, in_fore)
    out_fore = heapq.heappop(fore)
    for_sum += in_fore - out_fore

    in_back = (-1) * A[-N - i - 1]
    heapq.heappush(back, in_back)
    out_back = heapq.heappop(back)
    back_sum += in_back - out_back

fore_list.append(for_sum)
back_list.append(back_sum)

ans = -float('inf')
for i in range(N + 1):
    opt = fore_list[i] + back_list[N - i]
    ans = max(ans, opt)
print(ans)
"""

"""
# ABC123 D - Cake 123
X, Y, Z, K = getNM()
A = sorted([-i for i in getList()])
B = sorted([-i for i in getList()])
C = sorted([-i for i in getList()])

pos = []
heapify(pos)
dict = defaultdict(int)
u = (A[0] + B[0] + C[0], 0, 0, 0)
heappush(pos, u)
dict[u] = 1

for i in range(K):
    p, i, j, l = heappop(pos)
    print(-p)
    # 取り出すごとにA, B, Cについての次の値をpush
    if i + 1 < X:
        opt_a = (A[i + 1] + B[j] + C[l], i + 1, j, l)
        if dict[opt_a] == 0:
            heappush(pos, opt_a)
            dict[opt_a] = 1
    if j + 1 < Y:
        opt_b = (A[i] + B[j + 1] + C[l], i, j + 1, l)
        if dict[opt_b] == 0:
            heappush(pos, opt_b)
            dict[opt_b] = 1
    if l + 1 < Z:
        opt_c = (A[i] + B[j] + C[l + 1], i, j, l + 1)
        if dict[opt_c] == 0:
            heappush(pos, opt_c)
            dict[opt_c] = 1
"""
# ABC149 E - Handshake
# Mがクソデカイので使用不可
# 二分探索使ってね
N, M = getNM()
A = sorted([-i for i in getList()])

pos = []
heapify(pos)
dict = defaultdict(int)
u = (A[0] + A[0], 0, 0)
heappush(pos, u)
dict[u] = 1

ans = 0
# 大きい値M番目まで全て求まる
for i in range(M):
    p, i, j = heappop(pos)
    ans += -p
    if i + 1 < N:
        opt_a = (A[i + 1] + A[j], i + 1, j)
        if dict[opt_a] == 0:
            heappush(pos, opt_a)
            dict[opt_a] = 1
    if j + 1 < N:
        opt_b = (A[i] + A[j + 1], i, j + 1)
        if dict[opt_b] == 0:
            heappush(pos, opt_b)
            dict[opt_b] = 1
print(ans)
