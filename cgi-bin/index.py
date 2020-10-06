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

# 蟻本

N = 5
K = 3
A = [1, 3, 5, 4, 2]
# [1, 3, 5]の最小値
# [2, 5, 4]の最小値
# [5, 4, 2]の最小値
pos = deque([0])

# posの内部のa1, a2...についてa1 < a2...かつ
# A[a1] < A[a2]...になるように
for i in range(1, K):
    if A[pos[-1]] < A[i]:
        pos.append(i)
    else:
        pos[-1] = i

for i in range(N - K):
    # iを削除してi + Kを入れる
    # もしposの先頭がiなら
    if pos[0] == i:
        pos.popleft()

    if A[pos[-1]] < A[i + K]:
        pos.append(i + K)
    else:
        pos[-1] = i + K

# AGC038 B - Sorting a Segment
N, K = getNM()
P = getList()
if N == K:
    print(1)
    exit()
"""
連続するK要素をsort
組み合わせの数は
ダブるやつ消す

BITとか？
dpする?

区間[i, i + K)と区間[j, j + K)がequivalentになるにはどうすればいいか
まず区間[i, i + K)と区間[j, j + K)は共通部分をもつ必要がある
[i, j)はもともと昇順に並んでいて、かつ[j, i + K)のどの値よりも小さい必要がある
同様に、[i + K, j + K)はもともと昇順に並んでいて、かつ[j, i + K)のどの値よりも大きい必要がある
するとi ~ j間の値xについて、xはiともjともequivalent
つまりi ~ j - 1についてjとequivalent
j - 1とjがequivalentなものを探す
j - 1 < 任意のj ~ j + Kの値 であればいい
j < 任意のj + 1 ~ j + K + 1の値 であればいい

左端にある数字が最小で、右端にある数字が最大ならいい

順列が全く変わらないケース: 共通部分を持たなくていい
順列が変わるケース: 共通部分を持つ
"""
# 順列が全く変わらないケース:
rev = [] # P[i](大), P[i + 1](小)の時、iを範囲に含まなければいい
for i in range(K):
    if P[i + 1] < P[i]:
        rev.append(i)

rev_group = set()
for i in range(N - K + 1):
    if not rev or rev[-1] < i:
        rev_group.add(i)
    if i + K < N and P[i + K] < P[i + K - 1]:
        rev.append(i + K - 1)
ans = N - K + 1 - max(len(rev_group) - 1, 0)

# 順列が変わるケース: 共通部分を持つ
# スライド最小値
# [i,i+K+1)の最大値、最小値を求める
min_l = [float('inf')] * N
pos1 = deque([])
for i in range(N):
    while pos1 and P[pos1[-1]] > P[i]:
        pos1.pop()
    pos1.append(i)
    if i - (K + 1) >= 0 and pos1[0] == i - (K + 1):
        pos1.popleft()
    if i - (K + 1) + 1 >= 0:
        min_l[i - (K + 1) + 1] = P[pos1[0]]

max_l = [0] * N
pos2 = deque([])
for i in range(N):
    while pos2 and P[pos2[-1]] < P[i]:
        pos2.pop()
    pos2.append(i)
    if i - (K + 1) >= 0 and pos2[0] == i - (K + 1):
        pos2.popleft()
    if i - (K + 1) + 1 >= 0:
        max_l[i - (K + 1) + 1] = P[pos2[0]]

# [i,i+K+1)の最大値がP[i + K]、最小値がP[i]の時iとi+1はequivalent
for i in range(N - K):
    if i in rev_group or i + 1 in rev_group:
        continue
    if P[i] == min_l[i] and P[i + K] == max_l[i]:
        ans -= 1
print(ans)
