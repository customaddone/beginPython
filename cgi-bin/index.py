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

layers = [1] * 51
patties = [1] * 51
for i in range(1, 51):
    # レベルiバーガーの総枚数、パティの数を計算
    layers[i] = 3 + layers[i - 1] * 2
    patties[i] = 1 + patties[i - 1] * 2


def count_patties(l, x):
    # レベル0バーガーなら
    if l == 0 and x == 1:
        return 1
    # レベル0以外の場合、x <= 1なら
    if x <= 1:
        return 0
    y = layers[l - 1]
    # もしB(レベルl - 1バーガー)P(レベルl - 1バーガー)B
    #             ↑
    # にxがあれば
    if x <= y + 1:
        # 左端の一枚を除いて
        return count_patties(l-1, max(x - 1, 0))
    else:
        # 一枚目のl - 1バーガーの内部に                # 2枚目のl - 1バーガーのパティの数 + 中央の1枚
        return count_patties(l-1, min(x-y-2, y)) + patties[l-1] + 1

N, X = getNM()
print(count_patties(N, X))
