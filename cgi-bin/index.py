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
dpで何とかいけそう
A:これまでのゲーム数
W:これまでの勝ち数
a:今回のゲーム数
w:今回の勝ち数
とすると
W * a < w * A(W / A < w / a)にしたい
W * a / A < w

dp[i][j]: i日目まででj回勝った時の期限が良かった日の最大値
どういう風に振り分けるか
i日目に勝つか負けるか
負ける場合はその回0勝でOK
その回までで機嫌がいい日がi日あった場合に必要な勝ち数の最小値
"""

N, K = getNM()
A = [0] + getArray(N)
imos = deepcopy(A)
for i in range(1, N + 1):
    imos[i] += imos[i - 1]

# 勝った回数の下限があるのに気をつける
under = [0] * (N + 1)
psu = K
for i in range(N, 0, -1):
    diff = min(psu, A[i])
    psu -= diff
    under[i] += diff
for i in range(1, N + 1):
    under[i] += under[i - 1]

prev = [float('inf') for i in range(N + 1)]
prev[0] = 0
prev[1] = max(1, under[1]) # 最初の1勝は1回勝つだけでいい

for i in range(2, N + 1):
    next = [float('inf') for i in range(N + 1)]
    for j in range(N):
        # 負けたい場合
        next[j] = min(next[j], prev[j])
        # 勝ちたい場合 相手はprev[j - 1](これまでの勝ち数)
        # 0 → 1の場合は1追加 最低でも1は追加される
        if j > 0:
            want = ((prev[j - 1] * A[i]) // imos[i - 1]) + 1
            if want <= A[i]: # 今回の試合数の範囲内なら
                next[j] = min(next[j], prev[j - 1] + want)
        next[j] = max(next[j], under[i]) # 下限を見る
        
    prev = next

ans = 0
for i in range(N + 1):
    if prev[i] <= K:
        ans = i
print(ans)
