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

# ABC167 teleporter
N, K = 6, 727202214173249351
A = [6, 5, 2, 5, 3, 2]
A = [i - 1 for i in A]

logk = K.bit_length()
doubling = [[-1] * N for _ in range(logk)]

# ダブリング
# 2 ** 0は１つ後の行き先
for i in range(N):
    doubling[0][i] = A[i]
for i in range(1, logk):
    for j in range(N):
        # doubling[i]はdoubling[i - 1]を２回行えばいい
        # doubling[i - 1][j]移動してその座標からまたdoubling[i - 1]移動
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

index = 0
# 各bitごとに移動を行う
for i in range(logk):
    if K & (1 << i):
        index = doubling[i][index]
print(index + 1)

S = 'RRLLLLRLRRLL'
N = len(S)
logk = (10 ** 5).bit_length()

doubling = [[-1] * N for _ in range(logk)]

# １回目の移動
for i in range(N):
    doubling[0][i] = i + 1 if S[i] == "R" else i - 1

# 2 ** k回目の移動
for i in range(1, logk):
    for j in range(N):
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

ans = [0] * N

# 10 ** 5回ぐらい回せば十分
for i in range(N):
    ans[doubling[logk - 1][i]] += 1

print(*ans)

# p307 ダブリング
N = 3
M = 10
que = [
[0, 3],
[3, 7],
[7, 0]
]

alta = []
for i in range(N):
    s, t =  que[i]
    if s < t:
        alta.append([s, t])
        alta.append([s + M, t + M])
    else:
        alta.append([s, t + M])
alta.sort(key = lambda i: i[1])

N = len(alta)

logk = (10 ** 6).bit_length()
doubling = [[-1] * N for _ in range(logk)]
for i in range(N):
    s, t = alta[i]
    for j in range(i + 1, N):
        opt_s, opt_t = alta[j]
        if t <= opt_s:
            doubling[0][i] = j
            break

for i in range(1, logk):
    for j in range(N):
        # 欄外に飛ぶようなら-1
        if doubling[i - 1][j] == -1:
            doubling[i][j] = -1
        else:
            doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

ans = 0
# 区間iからスタート
for i in range(N):
    s, t = alta[i]
    now = i
    cnt = 1
    # 超過しないよう大きいものから加算していく
    for j in range(logk - 1, -1, -1):
        opt_index = doubling[j][now]
        # 欄内に収まるかつ始点から距離M以内
        if opt_index >= 0 and alta[opt_index][1] <= M:
            now = opt_index
            cnt += 1 << j
    ans = max(ans, cnt)
print(ans)
