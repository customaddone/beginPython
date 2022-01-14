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
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
N組の百合カップルがあり、それぞれ
座標A_i<B_iに居ます。
またM人の男がいて座標C_iに居ます。
i番目のカップルは間に男がいなければ尊さがP_i加算されますが男がいたら0加算されます。
K=0...Mについて
K人の男を◯せる時尊さの和の最大を求めてください

N<=200000
M<=18
A_i,B_i,C_iは全て異なる
"""

N = 10
Y = [[1, 5], [7, 18], [3, 9], [4, 32], [40, 79], [13, 21], [8, 10], [19, 35], [11, 43], [15, 28]]
P = [9, 19, 49, 39, 28, 49, 13, 2, 8, 48]
M = 8
Man = [2, 6, 12, 14, 34, 35, 41, 77]

Man.sort()
m = [0] + Man + [inf] # 番兵を足す
# 「女aはm[i] < a < m[i + 1]におり、女bはm[j] < b < m[j + 1]の位置にいる」　ものを全て同一視すると(M + 1)^2種類しかない
# dp[i][j]: 女aはm[i] < a < m[i + 1]におり、女bはm[j] < b < m[j + 1]の位置にいる
dp = [[0] * (M + 1) for i in range(M + 1)]
for i in range(N):
    dp[bisect_left(m, Y[i][0]) - 1][bisect_left(m, Y[i][1]) - 1] += P[i]

ans = [0] * (M + 1)
for bit in range(1 << M):
    ma_bit = [0] + [Man[i] for i in range(M) if bit & (1 << i)] + [inf]
    # dpを二重ループして数え上げ
    opt = 0
    label = [bisect_right(ma_bit, m[i]) for i in range(M + 1)] # m[i]の前にma_bitの要素が何個あるか
    for i in range(M + 1):
        for j in range(i, M + 1):
            # 男が挟まってなかったら
            if label[i] == label[j]:
                opt += dp[i][j]

    ans[bin(bit).count('1')] = max(ans[bin(bit).count('1')], opt)

print(*ans)
