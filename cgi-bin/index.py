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
import copy
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

ans = 0
def dfs(i, numlist):
    if i == N:
        # numlistを元に得点計算
        cnt = 0
        for jud in lista:
            if numlist[jud[1]] - numlist[jud[0]] == jud[2]:
                cnt += jud[3]
        return cnt

    ans = 0
    # もしi = 0なら
    sta = 0
    # もしi != 0なら一個前の数字を参照
    if i > 0:
        sta = numlist[i - 1]
    # 1つ前の数字が1なら1 ~ 10までをdfs
    # 重複組み合わせ
    for j in range(sta, M):
        # 数字を記録
        numlist[i] = j
        ans = max(ans, dfs(i + 1, numlist))
    return ans
print(dfs(0, [0] * N))
