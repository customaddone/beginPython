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
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
各集合について
(maxy - miny + 1) * (maxx - minx + 1) の領域内の点の数をかぞえあげる
最大N
全ての部分集合は2^N個あるが、長方形の領域がダブル場合がある

もしx座標だけでいいのなら
[1, 2, 3, 4] 両端を決める その内部にある点があるかないか

各頂点が何回含まれるかを見る
自身がついているなら必ず含まれる
自身がついてない場合は？

上下左右のみを2^Nしたやつ　- 右上のみ - 右下のみ...がいらないやつ
"""

N = getN()
P = [getList() for i in range(N)]
