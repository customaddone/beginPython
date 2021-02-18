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

# 決め打ち二分探索
# ABC146 C - Buy an Integer

A, B, X = getNM()

ok = 0
ng = 10 ** 9 + 1

def f(x):
    return A * x + B * len(str(x)) <= X

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)

# ABC034 D-食塩水
# 小数ver

N, K = getNM()
query = [getList() for i in range(N)]

def judge(target):
    alta = []
    for i in range(N):
        salt = query[i][0] * (query[i][1] - target)
        alta.append(salt)
    alta.sort(reverse = True)
    return sum(alta[:K]) >= 0

left = -1
right = 101 # 大きい値を

for i in range(100):
    mid = left + (right - left) / 2
    if judge(mid):
        left = mid
    else:
        right = mid
print(left)
