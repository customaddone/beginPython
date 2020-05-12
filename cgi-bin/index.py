def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

N = getN()
splitlist = [1]
splitsix = 6
while splitsix < 100000:
    splitlist.append(splitsix)
    splitsix *= 6
splitnine = 9
while splitnine < 100000:
    splitlist.append(splitnine)
    splitnine *= 9
splitlist.sort()
# これやらないと再帰が無限に実行される
splitlist.reverse()

ans = float('inf')
dp = [float('inf')] * (N + 1)
dp[0] = 0

# 貰うdp
for i in range(N + 1):
    for k in splitlist:
        if i >= k:
            dp[i] = min(dp[i], dp[i - k] + 1)
print(dp[-1])
