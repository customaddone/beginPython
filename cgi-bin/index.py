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
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

# ABが水、CDが砂糖、Eがとけられる量、Fが上限
A, B, C, D, E, F = getNM()

# A,Bを好きな回数使うことでi(0 <= i <= 30)の水を作り出せる
dp1 = [0] * 31
dp1[0] = 1
for i in range(1, 31):
    if i >= A:
        dp1[i] = max(dp1[i], dp1[i - A])
    if i >= B:
        dp1[i] = max(dp1[i], dp1[i - B])
waterlist = []
for i in range(31):
    if dp1[i] > 0:
        waterlist.append(i)

# C,Dを好きな回数使うことでi(0 <= i <= 3000)の砂糖を作り出せる
dp2 = [0] * 3001
dp2[0] = 1
for i in range(1, 3001):
    if i >= C:
        dp2[i] = max(dp2[i], dp2[i - C])
    if i >= D:
        dp2[i] = max(dp2[i], dp2[i - D])
sugerlist = []
for i in range(3001):
    if dp2[i] > 0:
        sugerlist.append(i)

ans = [0, 0]
concent = 0

for water in waterlist[1:]:
    if 100 * water <= F:
        left = F - (water * 100)
        # Fから水をひいた分、溶ける砂糖の限界を超えない量の砂糖を取得する
        index = bisect_right(sugerlist, min(left, E * water))
        suger = sugerlist[index - 1]
        # 濃度計算
        optconc = (100 * suger) / (100 * water + suger)
        # ここ>にすると濃度0%に対応できずWAに
        if optconc >= concent:
            concent = optconc
            ans = [100 * water + suger, suger]
print(*ans)
