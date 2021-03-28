from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
import random
import string
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

N = 3
P = [[1, 2, 300], [3, 3, 600], [1, 4, 800]]

# フラグが立ってないところについて最寄りのフラグを教えてくれる
def close(bit, mother, n):
    # n = bit.bit_length()
    res = [[] for i in range(n)]
    build = -1
    not_build = []
    for i in range(n):
        # フラグが立っている
        if bit & (1 << i):
            build = i
            # 右側のフラグについて
            while not_build:
                p = not_build.pop()
                res[p].append(build)
        elif mother & (1 << i):
            # 左側のフラグについて
            if build >= 0:
                res[i].append(build)
            not_build.append(i)

    return res

# x_cnt[i][j]: 集合iであり、j本引かれている場合
x_cnt = [[float('inf')] * (N + 1) for i in range(1 << N)]
# 集合xがあり、その中のj or bit ^ j本に線が引かれている場合
for bit in range(1 << N):
    j = bit # 例: 1010(10)
    while j:
        cost = [0] * N
        line = close(j, bit, N)
        for i in range(N):
            # 線が引かれてたらコスト0
            if j & (1 << i):
                continue
            cost[i] = abs(P[i][0]) * P[i][2]
            for o in line[i]:
                cost[i] = min(cost[i], abs(P[i][0] - P[o][0]) * P[i][2])

        cnt = bin(j).count('1')
        x_cnt[bit][cnt] = min(x_cnt[bit][cnt], sum(cost))

        cost = [0] * N
        line = close((bit ^ j), bit, N)
        for i in range(N):
            if (bit ^ j) & (1 << i):
                continue
            cost[i] = abs(P[i][0]) * P[i][2]
            for o in line[i]:
                cost[i] = min(cost[i], abs(P[i][0] - P[o][0]) * P[i][2])

        cnt = bin(bit ^ j).count('1')
        x_cnt[bit][cnt] = min(x_cnt[bit][cnt], sum(cost))

        j -= 1 # 1010 → 1001 1だけ減らして数字を変える
        j &= bit # 1010 → 1000 実質引き算 同じ要素があるところまで数字を減らす

y_cnt = [[float('inf')] * (N + 1) for i in range(1 << N)]

for bit in range(1 << N):
    j = bit # 例: 1010(10)
    while j:
        cost = [0] * N
        line = close(j, bit, N)
        for i in range(N):
            if j & (1 << i):
                continue
            cost[i] = abs(P[i][1]) * P[i][2]
            for o in line[i]:
                cost[i] = min(cost[i], abs(P[i][1] - P[o][1]) * P[i][2])

        cnt = bin(j).count('1')
        y_cnt[bit][cnt] = min(y_cnt[bit][cnt], sum(cost))

        cost = [0] * N
        line = close((bit ^ j), bit, N)
        for i in range(N):
            if (bit ^ j) & (1 << i):
                continue
            cost[i] = abs(P[i][1]) * P[i][2]
            for o in line[i]:
                cost[i] = min(cost[i], abs(P[i][1] - P[o][1]) * P[i][2])

        cnt = bin(bit ^ j).count('1')
        y_cnt[bit][cnt] = min(y_cnt[bit][cnt], sum(cost))

        j -= 1 # 1010 → 1001 1だけ減らして数字を変える
        j &= bit # 1010 → 1000 実質引き算 同じ要素があるところまで数字を減らす

for bit in range(1 << N):
    for i in range(N + 1):
        if x_cnt[bit][i] == float('inf'):
            x_cnt[bit][i] = 0
        if y_cnt[bit][i] == float('inf'):
            y_cnt[bit][i] = 0

print(x_cnt, y_cnt)
ans = [float('inf')] * 31
for bit in range(1 << N):
    x = bit
    y = bit ^ ((1 << N) - 1)
    for i in range(N + 1):
        for j in range(N + 1):
            ans[i + j] = min(ans[i + j], x_cnt[x][i] + y_cnt[y][i])
print(ans)
