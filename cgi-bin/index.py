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
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# n * nのボード　一片2000
# 同じ数字だけを組み合わせて三角形を作るが、マスのどれか一つを変更できる
# 一片は辺に平行でないといけない

# つまり、数字dを
# 1: 同じ列から2つ、1つ選ぶ　
# 2: 同じ行から2つ、1つ選ぶ　
# 1: 頂点を2つ選べる列があるとする　その列の最大辺となるような　頂点2つを選ぶ
# そしてもっとも距離が離れた辺を選ぶ
# ワイルドカードがなければこれは一意に定まる

# 各列について
# ワイルドカードを同じ列で使う場合
# 一番右、もしくは一番左の点を選ぶ　そして高さを求める
# 違う列で使う場合
# 底辺が定まる　max(上との距離、下との距離）をかける

N = getN()
M = [list(map(int, list(input()))) for i in range(N)]
row = [[[] for i in range(10)] for i in range(N)] # 行
col = [[[] for i in range(10)] for i in range(N)] # 列
# 各数字の上下左右の最大値
lim = [[float('inf'), -float('inf'), float('inf'), -float('inf')] for i in range(10)]

for i in range(N):
    for j in range(N):
        row[i][M[i][j]].append(j)
        col[j][M[i][j]].append(i)
        lim[M[i][j]][0] = min(lim[M[i][j]][0], i)
        lim[M[i][j]][1] = max(lim[M[i][j]][1], i)
        lim[M[i][j]][2] = min(lim[M[i][j]][2], j)
        lim[M[i][j]][3] = max(lim[M[i][j]][3], j)

ans = [0] * 10
for n in range(10):
    # 行と列といっぺんにやる
    for i in range(N):
        # 同列ワイルドカード
        if len(row[i][n]) >= 1:
            ans[n] = max(ans[n], max(row[i][n][0], N - row[i][n][-1]) * )
