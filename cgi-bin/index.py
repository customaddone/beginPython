def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, deque
from sys import exit
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
N, M, X = getNM()
book = []
cost = []
for i in range(N):
    c, *a, = getList()
    book.append(a)
    cost.append(c)
ans = float('inf')
for bit in range(1 << N):
    know = [0] * M
    costbit = 0
    flag = True
    for i in range(N):
        if bit & (1 << i):
            for j in range(M):
                know[j] += book[i][j]
            costbit += cost[i]
    for l in range(M):
        if know[l] < X:
            flag = False
    if flag:
        ans = min(ans, costbit)
if ans <= 1000000000:
    print(ans)
else:
    print(-1)
