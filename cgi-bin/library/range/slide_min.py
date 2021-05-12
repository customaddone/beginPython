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

# スライド最小値

N = 5
K = 3
A = [1, 3, 5, 4, 2]

# 順向き
# [0, K), [1, K + 1), [2, K + 2)の最小値をそれぞれm[0], m[1], m[2]...とする
# m[0] ~ m[K - 1]をO(N)で求める
def slide_min(arr, ran):
    n = len(arr)
    q = deque([])
    res = [float('inf')] * n

    # 前にある新規のものより大きい数字はもう必要ない
    for i in range(n):
        while q and arr[q[-1]] >= arr[i]:
            q.pop()
        # 範囲から外れたものを外すためにインデックスを入れる
        q.append(i)

        # 記入
        if i - ran + 1 >= 0:
            res[i - ran + 1] = arr[q[0]]
        # K未満の長さの区間も許すなら
        # res[i] = arr[q[0]]

        # 削除
        if q[0] <= i - ran + 1:
            q.popleft()

    return res

# 逆向き
def slide_rev_min(arr, ran):
    n = len(arr)
    q = deque([])
    res = [float('inf')] * n

    # 前にある新規のものより大きい数字はもう必要ない
    for i in range(n - 1, -1, -1):
        while q and arr[q[-1]] >= arr[i]:
            q.pop()
        q.append(i)
        # 記入
        if i + ran - 1 < n:
            res[i + ran - 1] = arr[q[0]]
        # K未満の長さの区間も許すなら
        # res[i] = arr[q[0]]

        # 削除
        if q[0] >= i + ran - 1:
            q.popleft()

    return res

# 使い方　競プロ典型90 037 - Don't Leave the Spice（★5）
# 今回は最大値を使うので数字を反転させている
# next[i] = min(prev[i - r] ~ prev[i - l]) + vをやりたい
W, N = getNM()

prev = [float('inf')] * (W + 1)
prev[0] = 0
for _ in range(N):
    l, r, v = getNM()
    next = [i for i in prev]
    # 右端がiの時の最大値(最小値の反転)を計算する
    # 今回はres[i] = arr[q[0]]を使う
    prev = slide_min(prev, r - l + 1)
    for i in range(1, W + 1):
        if i - l >= 0:
            # next[i] = min(prev[i - r] ~ prev[i - l]) + vをしている
            next[i] = min(next[i], prev[i - l] - v)
    prev = next

if prev[W] == float('inf'):
    print(-1)
else:
    print(-prev[W])
