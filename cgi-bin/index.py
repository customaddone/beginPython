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

N, M = getNM()
R = [getList() for i in range(M)]

imos = [0] * (N + 1)
for l, r in R:
    imos[l - 1] += 1
    imos[r] += 1

for i in range(1, N + 1):
    imos[i] += imos[i - 1]

section = [
[-3, 3],
[-1, 1],
[5, 7],
[1, 2],
]

query = [0, 1, 2, 3]
# [{0, 1}, {0, 3}, {0}, set()]

def event_sort(section, query):
    s = len(section)
    q = len(query)
    # イベント生成
    task = []
    for i in range(s):
        s, t = section[i]
        task.append((s, 0, i))
        task.append((t, 1, i))
    for i in range(q):
        task.append((query[i], 2, i))
    task.sort()

    # 引っかかってる場所の管理
    se = set()
    res = []

    for a, b, c in task:
        # ゴールが来ると削除
        if b == 1:
            se.remove(c)
        # スタートが来ると追加
        elif b == 0:
            se.add(c)
        # queについてなら
        else:
            res.append(deepcopy(se))

    return res

# query内の点iがどのsection内の点j内にあるか
event_sort(section, query)
