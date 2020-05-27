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
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


N, M, Q = getNM()
lista = []
for i in range(Q):
    a, b, c, d = getNM()
    lista.append([a - 1, b - 1, c, d])

def dfs(i, numlist):
    if i == N:
        # 集計
        cnt = 0
        for jud in lista:
            if numlist[jud[1]] - numlist[jud[0]] == jud[2]:
                cnt += jud[3]
        return cnt

    ans = 0
    sta = 0

    if i > 0:
        sta = numlist[i - 1]

    # 条件についてループさせてdfs
    for j in range(sta, M):
        numlist[i] = j
        ans = max(ans, dfs(i + 1, numlist))
    return ans
print(dfs(0, [0] * N))
