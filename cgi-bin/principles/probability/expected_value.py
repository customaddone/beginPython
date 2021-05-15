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
sys.setrecursionlimit(1000000)
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# 期待値
"""
期待値の求め方
E[i] = Σ ((iに遷移する可能性のある状態jについて、E[j]) + 1) * (j → iの遷移の確率)
逆もできる
E[i]: ゴールの状態からの期待値
E[i] = Σ ((iから遷移する可能性のある状態jについて、E[j]) + 1) * (i → jの遷移の確率)
iに繋がるどこかの道を塞ぐ場合
塞いだ道の期待値への寄与分 - 塞いだことによる他の道の増分 を考える
ABC144 F - Fork in the Road

期待値の線型性
確率aで条件を満たす操作がある
条件を満たすのにかかる操作の期待値は 1/aになる
"""
