def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)

n = int(input())
s = input()

op, cl = 0 ,0
# sを右から調べていく
# s[i]が何なら何が必要になるのか
for c in s:
    if c == '(':
        op += 1
    else:
        if op > 0:
            op -= 1
        else:
            cl += 1
# 追加するのは左に'('いくつか右に')'いくつか
print(('(' * cl) + s + (')' * op))
