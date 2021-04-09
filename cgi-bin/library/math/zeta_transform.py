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
MOD = 998244353
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
A = {0, 1, 2}
冪集合 = {}, {0}, {1}, {2}, {0, 1}...
f = [3, 1, 4, 1, 5...]

ある部分集合Siについて, Si <= Tとなる全てのf(T)の総和を求めたい
Si = {1} Siが含まれるもの全ての和
T = {1}, {0, 1}, {1, 2}, {0, 1, 2}
逆verもある Siの部分集合全てについて
Siの補集合を取ってゼータ変換をする

0b1 0b0
0b11 0b10
0b101 0b100
0b111 0b110
0b10 0b0
0b11 0b1 要素0b0の情報も持つ
0b110 0b100
0b111 0b101 要素0b100の情報も持つ
0b100 0b0
0b101 0b1
0b110 0b10 要素0b0の情報も持つ
0b111 0b11 要素0b0, 0b1の情報も持つ

0b111に各要素1回きり情報が伝播する

総和の値から元の値を割り出すのがメビウス変換
"""

# Siを部分集合にするものについて
n = 3  # 集合の要素数
dp = [3, 1, 4, 5, 1, 9, 2, 6]  # 2^n の長さ

for j in range(n):
    bit = 1 << j
    for i in range(1 << n): # 小さい順からやる
        if i & bit == 0: # 重ならないなら
            # i | bitよりサイズが一つ小さい部分集合に自身を足す
            # N回やることで条件を満たす全ての要素について操作できた
            dp[i] += dp[i | bit]

print(dp)
# => [31, 21, 17, 11, 18, 15, 8, 6]

# Siの各部分集合について
n = 3  # 集合の要素数
dp = [3, 1, 4, 5, 1, 9, 2, 6]  # 2^n の長さ

for j in range(n):
    bit = 1 << j
    for i in range(1 << n):
        if i & bit:
            dp[i] += dp[i ^ bit]

print(dp)
# => [3, 4, 7, 13, 4, 14, 10, 31]

# メビウス変換1
n = 3  # 集合の要素数
dp = [31, 21, 17, 11, 18, 15, 8, 6]  # ゼータ変換①後

for j in range(n):
    bit = 1 << j
    for i in range(1 << n):
        if i & bit == 0:
            dp[i] -= dp[i | bit]  # + を - にしただけ

print(dp)
# => [3, 1, 4, 5, 1, 9, 2, 6]

# メビウス変換2
n = 3  # 集合の要素数
dp = [3, 4, 7, 13, 4, 14, 10, 31]  # ゼータ変換②後

for j in range(n):
    bit = 1 << j
    for i in range(1 << n):
        if i & bit:
            dp[i] -= dp[i ^ bit]  # + を - にしただけ

print(dp)
# => [3, 1, 4, 5, 1, 9, 2, 6]
