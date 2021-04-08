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

N = getN()
P = [getList() for i in range(N)]

def euc(p1, p2):
    px1, py1 = p1
    px2, py2 = p2
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)

# 線分cpとcからx軸方向に伸びる半直線とのなす角の大きさ
def angle(c, p):
    d = euc(c, p)
    x = (p[0] - c[0]) / d
    y = (p[1] - c[1]) / d
    # sinθ >= 0なので角度は180度以内
    if y >= 0:
        return math.degrees(math.acos(x))
    else:
        return 360 - math.degrees(math.acos(x))

right = 0
obtuse = 0
# 点P[i]を中心に各線分について
for i in range(N):
    # 線分P[i]-P[j]とx軸の正の部分とのなす角を昇順に並べて二分探索or尺取り法
    l = []
    for j in range(N):
        if i == j:
            continue
        opt = angle(P[i], P[j])
        l.append(opt)
        l.append(opt + 360) #　一周後の
    l.sort()

    b1 = 0 # 90度のライン
    b2 = 0 # 270度のライン
    for j in range(N - 1):
        # ちょうど90度になるものはギリギリ超える
        while l[b1] <= l[j] + 90 + eps:
            b1 += 1
        # ちょうど270度になるものはギリギリ超えない
        while l[b2] < l[j] + 270 - eps:
            b2 += 1

        # 直角三角形を数える
        if abs(90 - (l[b1 - 1] - l[j])) < eps:
            right += 1
        if abs(270 - (l[b2] - l[j])) < eps:
            right += 1

        obtuse += (b2 - b1)

right //= 2
obtuse //= 2
all = N * (N - 1) * (N - 2) // 6
print(all - right - obtuse, right , obtuse)
