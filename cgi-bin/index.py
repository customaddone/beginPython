from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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

"""
期待値を求める問題
すべての場合が2^N通りある
それぞれについての穴の数がHi個ある
その総和をHとすると、答えはH / 2^N個
答えは逆元をかける

黒い頂点を全て繋ぐと求める部分木ができる
頂点iが穴あきになる場合の数
頂点iが穴あき = パス上に頂点iがある黒い点Bi, Bjがある
頂点iの子要素のうちどれか2つ以上が黒い木
"""

N = getN()
E = [[] for i in range(N)]
for i in range(N - 1):
    s, t = getNM()
    E[s - 1].append(t - 1)

def parents(n, sta, dist):
    pos = deque([sta])
    ignore = [0] * n
    path = [0] * n
    path[sta] = -1

    while pos:
        u = pos.popleft()
        ignore[u] = 1

        for i in dist[u]:
            if ignore[i] != 1:
                path[i] = u
                pos.append(i)

    return path

P = parents(N, 0, E)
print(P)
