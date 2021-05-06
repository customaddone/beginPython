from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353

INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

#####segfunc#####
# 範囲内の過半数を占める要素がありそうならその可能性を返す
# [1, 2, 3, 3]
# [1, 2]について過半数を占める要素なし (-1, 0)
# [3, 3]について過半数を占める要素は3
# (-1, 0)について、3の数は多かったとしても半分
# (1, 1)について, 3の数は多かったとしても半分 - 1
def segfunc(x, y):
    if x[0] == y[0]:
        return x[0], x[1] + y[1]
    elif x[1] > y[1]:
        return x[0], x[1] - y[1]
    elif x[1] < y[1]:
        return y[0], y[1] - x[1]
    else:
        return -1, 0
#################

#####ide_ele#####
ide_ele = (-1, 0)
#################

N, M = getNM()
A = getList()
L = [[] for i in range(N + 1)]
for i in range(N):
    L[A[i]].append(i)

A = [(a, 1) for a in A]
seg = SegTree(A, segfunc, ide_ele)

for _ in range(M):
    l, r = getNM()
    l -= 1
    v, c = seg.query(l, r)
    if c == 0:
        print(1)
    else:
        m = bisect_left(L[v], r) - bisect_left(L[v], l)
        print(max(m * 2 + l - r, 1))
