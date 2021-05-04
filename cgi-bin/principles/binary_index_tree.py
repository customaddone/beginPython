from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement

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

"""
転倒数
値vを置くことによって増える転倒数は左側にvより大きい値の数に依存し
左にある数の順番は関係がない

転倒数がRのものを作る
1 ~ Nを降順にソートして前から見ていく
[5, 4, 3, 2, 1] 1:転倒数+4, 2:転倒数+3...

いらない増分については値を一番左にappendleftする
"""

# 2を置くことで増える転倒数はどれも同じ
[5, 4, 3,  , 2]
[4, 5, 3,  , 2]
[3, 4, 5,  , 2]
