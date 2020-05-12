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

def spliter(n):
    if dp[n] < 1000000:
        return dp[n]
    res = float('inf')
    for split in splitlist:
        if n >= split:
            res = min(res, spliter(n - split) + 1)
    dp[n] = res
    return res
spliter(N)
print(dp[-1])
