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
tree一回流すのは意外と計算量いる
10 ** 5のtreeをlogN回は流せない
10 ** 6だとせいぜい2, 3回

頂点0からuまできた時の現在の状態（0からの距離、通ったedgeの本数、edgeの色の種類等）はdfsで求められる
全て保存はできないのでクエリ先読みなどして必要な分だけとる
"""
