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

A, B, H, M = getNM()
minu = H * 60 + M

# 時針の角度
angh = minu / 2
# 分針の角度
angm = M * 6

# 角度の差
anglepre = abs(angh - angm)
angle = min(360 - anglepre, anglepre)

# ラジアンに直してからmath.cosとかmath.tanとか
ans = (A ** 2) + (B ** 2) - (2 * A * B * math.cos(math.radians(angle)))

print(math.sqrt(ans))
