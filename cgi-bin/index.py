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

S = input()
T = input()

s = Counter(S)
t = Counter(T)

# azzelをappleにするとき
# 問題参照

# aplezをappleにする時
# c1 = z c2 = aにすると
# apleaにできる
# c1 = a, c2 = pにすると
# aalep ⇄ できない

# Sの文字列にaがi1個、bがi2個,,,
# Tの文字列にaがj1個、bがj2個,,,あるとすると
# sort(i1, i2...)とsort(j1, j2...)が一致していればいい
# 構成要素の個数の集合が一致していればいい
if sorted(s.values()) == sorted(t.values()):
	print("Yes")
else:
	print("No")
