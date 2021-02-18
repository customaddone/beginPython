from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# 区間の問題について
# ARC045 B - ドキドキデート大作戦高橋君

N, M = getNM()
R = [getList() for i in range(M)]

imos = [0] * (N + 2)
for l, r in R:
    imos[l] += 1
    imos[r + 1] -= 1

for i in range(1, N + 2):
    imos[i] += imos[i - 1]

imos_b = [0] * (N + 2)
for i in range(1, N + 1):
    if imos[i] <= 1:
        imos_b[i] += 1
# Rの各区間について区間内全てでフラグが0か？
# 累積和で求められる
# imos_b [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]

for i in range(1, N + 2):
    imos_b[i] += imos_b[i - 1]
# imos_b [0, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 8]

# 区間内全ての、は累積和でもできる
ans = 0
index = []
for i in range(M):
    l, r = R[i]
    if imos_b[r] - imos_b[l - 1] == 0:
        ans += 1
        index.append(i + 1)
print(ans)
for i in index:
    print(i)
