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

# 典型90問　11日目　賞味期限付きマージ型dp

N = getN()
day = [[] for i in range(5001)]
for _ in range(N):
    d, c, s = getNM()
    day[d].append([c, s])

# マージ型
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
