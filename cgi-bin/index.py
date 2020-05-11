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
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

from collections import deque

# まず、Kの最小値を求める
#　頂点に繋がる辺の数 <= Kを全ての頂点で満たす
N, K = getNM()
R, S, P = getNM()
T = input()
# 手を出したか出してないか
flag = [0] * N
ans = 0
for i in range(N):
    if i - K >= 0 and T[i - K] == T[i] and flag[i - K]:
        continue
    if T[i] == 'r':
        ans+=P
    elif T[i] == 's':
        ans+=R
    else:
        ans+=S
    flag[i] = True
print(ans)
