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
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

from itertools import permutations
from math import factorial, hypot

N, M = 3, 3
inf = 10 ** 20

# 距離
g = [
[0, 1, 3],
[1, 0, 2],
[3, 2, 0],
]

# dp[S][v][0]: 訪れた点の集合がS。現在vにいてそこから0に帰ってくるときの最小距離。
# dp[S][v][1]:何通りあるか
dp = [[[inf, 1] for i in range(N)] for i in range(1 << N)]
# 全ての道を訪れて0に戻った時の通りが1通り
dp[(1 << N) - 1][0]=[0, 1]

# 巡回状況　逆順に
for s in range((1 << N) - 2, -1, -1):
    # 現在の場所
    for j in range(N):
        # 次の道について
        for k in range(N):
            if not s & (1 << k):
                # 値が小さくなるなら更新。
                if dp[s][j][0] > dp[s | 1 << k][k][0] + g[j][k]:
                    dp[s][j][0] = dp[s | 1 << k][k][0] + g[j][k]
                    dp[s][j][1] = dp[s | 1 << k][k][1]
                # 値が同値なら、組み合わせに足す
                elif dp[s][j][0] == dp[s | 1 << k][k][0] + g[j][k]:
                    dp[s][j][1] += dp[s | 1 << k][k][1]

# 0から巡回して再び戻ってくる最短距離
if dp[0][0][0] < 10 ** 20:
    print(*dp[0][0])
else:
    print("IMPOSSIBLE")
