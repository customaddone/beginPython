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

N, X = getNM()
A = getList()
ans = 0
flag = True
while flag:
    flag = False
    for i in range(N - 2):
        # A[i1とA[i + 1]の過剰分
        minus1 = A[i] + A[i + 1] - X
        # A[i + 1]とA[i + 2]の過剰分
        minus2 = A[i + 1] + A[i + 2] - X
        if minus1 > 0 and minus2 > 0:
            # minus1とminus2が両方プラスなら一個食べるだけでminu1とminu2の分を
            # 両方減らせる
            minuspoint = min(minus1, minus2, A[i + 1])
            A[i + 1] -= minuspoint
            ans += minuspoint
            # これをminu1,minu2が両方プラスになる部分（お得な点)がなくなるまで繰り返す
            flag = True
between = [A[i] + A[i + 1] - X for i in range(N - 1)]
for i in between:
    if i > 0:
        ans += i
print(ans)
