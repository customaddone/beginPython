from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement


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

"""
山が一つの場合を考える
Aの操作しか行えない場合
wが偶数: 先手勝ち
wが奇数: 後手勝ち

wが偶数の場合
このままでは後手は負けてしまうので、Bの操作を行い手番を変える
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1...
b = 1, 3, 7...なら手番を変えることができる　それ以外はできない
dp[w][b]のdp

dp[0][1]の場合　操作を行えないので手番を変えられない
dp[1][1]の時、操作Aを行いdp[0][2]に遷移できる
dp[0][2]の時、操作Bを行いdp[0][1]に遷移できる
遷移した先に0(操作できない)があれば1 なければ0
bのmaxは50 * (50 + 1) // 2 = 1275
"""

# 手番を変更することが可能か
dp = [[0] * 1301 for i in range(51)]

# この山を全て消化した時に手番を入れ替えられるか
for w in range(51):
    for b in range(1301):
        # 操作1
        if w > 0 and b + w < 1301 and not dp[w - 1][b + w]:
            dp[w][b] = 1
        for j in range(1, (b // 2) + 1):
            # 操作2
            if b > 1 and not dp[w][b - j]:
                dp[w][b] = 1

N = getN()
A = getList()
B = getList()

for a, b in zip(A, B):
    print(dp[a][b])
