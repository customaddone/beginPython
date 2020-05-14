def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N = getN()
S1 = input()
S2 = input()
dp = [0 for i in range(N)]
if S1[0] == S2[0]:
    dp[0] = 3
else:
    dp[0] = 6
# i - 1個目、i個目が
# 横ドミノ１個目→横ドミノ２個目
# 横ドミノ→横ドミノ
# 横ドミノ→縦ドミノ
# 縦ドミノ→縦ドミノ
# 縦ドミノ→横ドミノそれぞれについて場合分け
# 各回について
for i in range(1, N):
    # 横ドミノ２つ目だった場合
    if S1[i] == S1[i - 1]:
        dp[i] = dp[i - 1]
    # 横ドミノ１つめor縦ドミノ１つ目の場合
    else:
        # 縦ドミノ１つ目
        if S1[i] == S2[i]:
            # 一つ前も縦ドミノ
            if S1[i - 1] == S2[i - 1]:
                dp[i] = (dp[i - 1] * 2) % mod
            # 横ドミノ
            else:
                dp[i] = dp[i - 1]
        # 横ドミノ1つ目
        else:
            # 一つ前が縦ドミノ
            if S1[i - 1] == S2[i - 1]:
                dp[i] = (dp[i - 1] * 2) % mod
            # 一つ前が２つ目横ドミノ
            else:
                dp[i] = (dp[i - 1] * 3) % mod
print(dp[-1])
