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
D = [7, 3, 5]
C = [3, 2, 3]
S = [20, 10, 15]
締め切りナシの場合は
weight: 日数 value: 金額のナップサック

i日目までに仕事を行うとして
締め切りがi日目以降のものについては期限なしと見れる
D = [7, 5]
C = [3, 3]
S = [20, 15] で5日目までに仕事を終わらすとすれば？

dpを考える　ナップサックであることには変わりはない
1, 2日目に締め切りが3日の仕事を終わらせる

i日目までに締め切りが来る仕事について　j日目まで仕事に使った時の最大値
(3, 2): 10
(5, 3): 15
(7, 5): 30
(7, 6): 35 小さなナップサックであらかじめ処理する
何日使うと何日増える　をあらかじめ計算する（アイテム12個で最大4000通りぐらいになる）

dp[i][j]の遷移元は
dp[i - 1]のj, j - 1, j - 2...について N^3解ができる　計算量を減らす

前から順番に賞味期限が早いものから考えて行けば
"""

N = getN()
day = [[] for i in range(5001)]
for _ in range(N):
    d, c, s = getNM()
    day[d].append([c, s])

def merge(bucket, items, day):
    prev = bucket
    # 新規アイテムについて
    for w, v in items:
        next = deepcopy(prev)
        # これまでのもの
        for iw, iv in prev.items():
            # 上限オーバーしなければ
            if w + iw <= day:
                next[w + iw] = max(next[w + iw], v + iv)
        prev = next

    return prev

# 締め切りがd日目までのアイテムでkey日消化した場合の最大値
dp = defaultdict(int)
dp[0] = 0
for d in range(5001):
    dp = merge(dp, day[d], d)

ans = 0
for v in dp.values():
    ans = max(ans, v)

print(ans)
