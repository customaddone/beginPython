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

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
from fractions import gcd
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

from itertools import permutations
from math import factorial, hypot

N, K = getNM()
query = []
for i in range(N):
    t = getList()
    query.append(t)

# n重ループは素直にデカルト積使え
# 下のでN重ループできる
def dfs(i, now):
    if i == 0:
        for m in query[0]:
            if m == 0:
                print('Found')
                exit()
            dfs(i + 1, m)
    elif i < N:
        for j in query[i]:
            newnow = j ^ now
            if newnow == 0:
                print('Found')
                exit()
            else:
                dfs(i + 1, newnow)
dfs(0, 0)
print('Nothing')

"""
N, K = map(int, input().split())
T = []
for i in range(N):
    t = list(map(int, input().split()))
    T.append(t)
flag = True
# 各配列のデカルト積
for ps in itertools.product(*T):
    x1 = ps[0]
    for i in range(1, N):
        x2 = ps[i]
        # 排他的論理和 x1, x2に含まれるもの - x1, x2両方に含まれるもの
        x1 = x1 ^ x2
    if x1 == 0:
        flag = False
print('Nothing' if flag else 'Found')
"""
