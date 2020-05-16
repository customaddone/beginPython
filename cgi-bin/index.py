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
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N, K = getNM()
X = getList()
ans = float('inf')

# 一直線に行くのが一番いいやり方
for i in range(N - K + 1):
    # もしX[i],X[i + K - 1]とも0以下の場合
    # 最短経路は0 ~ (X[i + K - 1]) ~ X[i]まで
    if X[i] <= 0 and X[i + K - 1] <= 0:
        ans = min(ans, -X[i])
    # もしX[i] < 0 <= X[i + K - 1]の場合
    # 最短経路は
    # X[i] ~ 0, 0 ~ X[i + K - 1]のうち近い方
    # + X[i] ~ X[i + K - 1]
    elif X[i] < 0 <= X[i + K - 1]:
        ans = min(ans, min(-X[i], X[i + K - 1]) + (X[i + K - 1] - X[i]))
    # もしX[i],X[i + K - 1]とも0以上の場合
    # 最短経路は0 ~ (X[i]) ~ X[i + K - 1]まで
    else:
        ans = min(ans, X[i + K - 1])
print(ans)
