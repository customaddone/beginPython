from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product
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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# 集合[a1, a2...an]内で以下２つの条件を満たす部分集合の組(T, U)はいくつあるか問題
# 1: U ⊆ Tである
# 2: Uがある条件を満たす

# Tの中にUがいくつか含まれる
# ①iが進むごとにTの候補がn倍ずつ増えていく
# ②その後、Uを組むためのカウントを進める

# ABC104 D - We Love ABC
S = '????C?????B??????A???????'
N = len(S)
# dp[i][j]: i番目にjまで丸をつけ終えている通り
dp = [[0] * 4 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    # 通りの数を増やす
    for j in range(4):
        if S[i] != '?':
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
        else:
            dp[i + 1][j] += 3 * dp[i][j]
            dp[i + 1][j] %= mod
    # カウントが進むものを加える
    if S[i] == 'A' or S[i] == '?':
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][1] %= mod
    if S[i] == 'B' or S[i] == '?':
        dp[i + 1][2] += dp[i][1]
        dp[i + 1][2] %= mod
    if S[i] == 'C' or S[i] == '?':
        dp[i + 1][3] += dp[i][2]
        dp[i + 1][3] %= mod
print(dp[N][3] % mod)

# ABC169 F - Knapsack for All Subsets
N, S = getNM()
A = getList()
MOD = 998244353

dp = [[0] * (S + 1) for i in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    # 通りの数を増やす
    for j in range(S + 1):
        dp[i + 1][j] += dp[i][j] * 2
        dp[i + 1][j] %= MOD
    # カウントが進むものを加える
    for j in range(S + 1):
        if j - A[i] >= 0:
            dp[i + 1][j] += dp[i][j - A[i]]
            dp[i + 1][j] %= MOD
print(dp[N][S] % MOD)

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
