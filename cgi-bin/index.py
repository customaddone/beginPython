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

N, A = getNM()
w = []
v = []
I = []
for i in range(N):
    o_v, o_w = getNM()
    w.append(o_w)
    v.append(o_v)
    I.append([o_v, o_w])

# items: [value, weight]
def half_knap(items, const):

    def merge(A, X): # merge A and A + X
        B = []
        i = 0
        nv, nw = X
        # aとその前の要素を比べる
        for v, w in A:
            while A[i][1] + nw < w or (A[i][1] + nw == w and A[i][0] + nv < v):
                B.append([A[i][0] + nv, A[i][1] + nw])
                i += 1
            B.append([v, w])
        # 残ったものを吐き出す
        while i < len(A):
            B.append([A[i][0] + nv, A[i][1] + nw])
            i += 1
        return B

    #　マージ
    L = [[0, 0]]
    R = [[0, 0]]
    for item in items[:10]:
        L = merge(L, item)
    for item in items[10:]:
        R = merge(R, item)

    # valの書き換え
    for i in range(1, len(R)):
        R[i][0] = max(R[i][0], R[i - 1][0])

    # 尺取り
    ans = 0
    for v, w in L:
        if w > const:
            break
        while w + R[-1][1] > const:
            R.pop()
        ans = max(ans, v + R[-1][0])

    return ans

# あるweightで獲得できる最大のvalue
def knapsack_wei(N, limit, weight, value):
    dp = [[0] * (limit + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(limit + 1):
            if weight[i] <= j:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][limit]

# あるvalueを獲得するために必要な最小のweight
def knapsack_val(N, limit, weight, value):
    max_v = sum(value)
    dp = [[float('inf')] * (max_v + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(max_v + 1):
            if value[i] <= j:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - value[i]] + weight[i])
            else:
                dp[i + 1][j] = dp[i][j]
    for i in range(max_v - 1, -1, -1):
        if dp[N][i] <= limit:
            return i

if N <= 30:
    print(half_knap(I, A))
    exit()
elif max(w) <= 1000:
    print(knapsack_wei(N, A, w, v))
    exit()
else:
    print(knapsack_val(N, A, w, v))
    exit()
