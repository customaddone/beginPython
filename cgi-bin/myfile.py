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

S = 'aabbcc'
s_n = len(S)
K = 'abc'
k_n = len(K)

# dp[i][j]: Sのi文字目までで部分文字列(Kのj文字目まで)を取り出せる通りの数
prev = [0] * (k_n + 1)
prev[0] = 1

for i in range(s_n):
    # S[i]を選択しない
    # 前の状態から変化なしなのでそのまま引き継ぐ
    next = prev
    for j in range(k_n):
        # S[i]を選択する 状態数が増える
        if S[i] == K[j]:
            next[j + 1] += prev[j]

    prev = next

print(prev[-1])
