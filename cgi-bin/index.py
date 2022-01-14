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
Nがくそでか　bitで考える　桁dp?
x // 2^k あるbit以下を切り捨て　後ろ4つが 1010
つまり　1010を持つ数がいくつあるか　桁dp
'', '1', '10', '101', '1010' の5つ
耳桁dp
"""

S = '1' * getN()
if S == '':
    print(0)
    exit()

N = len(S)
# 次にあるべき数字
jud = [1, 0, 1, 0, inf]
# dp[i][j][k]: iまで進んで最大値になる可能性がある(0)/ない(1), 状態はk
dp = [[[0] * 5 for _ in range(2)] for i in range(N + 1)]
dp[0][0][0] = 1

for i in range(N):
    d = int(S[i])
    # Lになる可能性があるかないか
    # ある→ある
    for j in range(2):
        # 次の桁は何にする　あるの場合はd以下　ないの場合は0, 1
        for d_j in range(2 if j else d + 1):
            # 状態1~4
            for k in range(4):
                # 次に進める
                if d_j == jud[k]:
                    dp[i + 1][j | (d_j < d)][k + 1] += dp[i][j][k]
                    dp[i + 1][j | (d_j < d)][k + 1] %= mod
                # 進めない
                else:
                    # 次が0なら状態0, 1なら状態1
                    dp[i + 1][j | (d_j < d)][(d_j == 1)] += dp[i][j][k]
                    dp[i + 1][j | (d_j < d)][(d_j == 1)] %= mod
            # 状態5
            dp[i + 1][j | (d_j < d)][4] += dp[i][j][4]
            dp[i + 1][j | (d_j < d)][4] %= mod

print((dp[i + 1][0][-1] + dp[i + 1][1][-1]) % mod)
