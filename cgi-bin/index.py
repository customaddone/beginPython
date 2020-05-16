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

A, B = getNM()
# bit1桁目のフラグの個数
# 周期は2 ** 1
# 0と1が交互に
# bit2桁目のフラグの個数
# 周期は2 ** 2
flags1 = [0] * 61
flags2 = [0] * 61
# 1 ~ nまでに各桁のフラグが何本立つか計算する関数
def bitflag(n, flaglist):
    if n > 0:
        for i in range(1, 61):
            split = 2 ** i
            flag1 = (n // split) * (split // 2)
            flag2 = max(n % split + 1 - (split // 2), 0)
            flaglist[i] += flag1 + flag2
# 1 ~ A - 1について（Aは範囲に入っているため）
bitflag(A - 1, flags1)
bitflag(B, flags2)

for i in range(61):
    flags2[i] -= flags1[i]
ans = 0
# 奇数ならフラグが立つ
for i in range(61):
    if flags2[i] % 2 != 0:
        ans += 2 ** (i - 1)
print(ans)
