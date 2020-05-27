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

from itertools import permutations
from math import factorial, hypot

lista = [[0, 0] for i in range(61)]
# bitの各桁が１か０かをlistaに収納
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            lista[i][1] += 1
        else:
            lista[i][0] += 1
splitbit(31)
print(lista)

flags1 = [0] * 61
# 1 ~ nまでに各桁のフラグが何本立つか計算する関数
def bitflag(ny, flaglist):
    if ny > 0:
        for i in range(1, 61):
            split = 2 ** i
            flag1 = (ny // split) * (split // 2)
            flag2 = max(ny % split + 1 - (split // 2), 0)
            flaglist[i - 1] += flag1 + flag2
bitflag(31, flags1)
print(flags1)
