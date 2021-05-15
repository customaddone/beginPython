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

# 耳dp
"""
配列A = [a1, a2, a3...]を連続するいくつかの状態に分けるのに有効
各状態について
dp[i][j]: 現在状態iでAをjまで調べたもの
前から引き続き状態iのものと今回状態i - 1 → iに遷移したものを比べる
dp[i][j] = min or max(dp[i][j - 1] + val1, dp[i - 1][j - 1])
"""

# みんなのプロコン 2019 D - Ears

L = getN()
A = getArray(L)

dp = [[float('inf')] * 5 for i in range(L + 1)]
# 状態0: 0区間、
# 状態1: 偶数区間、
# 状態2: 奇数区間。
# 状態3: 偶数区間、
# 状態4: 0区間
dp[0][0] = 0

# 偶数区間で0なら2を払ってもらう
def zero_e(a):
    if a == 0:
        return 2
    else:
        return (a % 2 != 0)
# 奇数区間で0なら1を払ってもらう
def zero_o(a):
    if a == 0:
        return 1
    else:
        return (a % 2 == 0)

# dp[i + 1]を更新していく
# 状態k(k <= j)から遷移することができる
for i in range(L):
    # 状態0 遷移はない
    dp[i + 1][0] = dp[i][0] + A[i]
    # 状態1
    dp[i + 1][1] = min(dp[i][1], dp[i][0]) + zero_e(A[i])
    # 状態2
    dp[i + 1][2] = min(dp[i][2], dp[i][1], dp[i][0]) + zero_o(A[i])
    # 状態3
    dp[i + 1][3] = min(dp[i][3], dp[i][2], dp[i][1], dp[i][0]) + zero_e(A[i])
    # 状態4
    dp[i + 1][4] = min(dp[i][4], dp[i][3], dp[i][2], dp[i][1], dp[i][0]) + A[i]

print(min(dp[L]))

"""
全ての部分集合の中の条件を満たす要素の数を数える

部分集合の数については
Aのj番目を含める/含めない　もしくはAのj番目を何の要素に変換するか
で増えていく

その中でi番目の要素まで満たした部分集合がいくつあるかを数える
つまり状態の遷移
"""

# ABC169 F - Knapsack for All Subsets
N, S = getNM()
A = getList()
MOD = 998244353

dp = [[0] * (S + 1) for i in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    # それぞれの部分文字列の数をcompoundする
    for j in range(S + 1):
        dp[i + 1][j] += dp[i][j] * 2
        dp[i + 1][j] %= MOD
    # i番目を部分集合に含める場合について　カウントが進むものを加える
    for j in range(S + 1):
        if j - A[i] >= 0:
            dp[i + 1][j] += dp[i][j - A[i]]
            dp[i + 1][j] %= MOD
print(dp[N][S] % MOD)
