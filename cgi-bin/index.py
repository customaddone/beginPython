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
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

N = getN()
A = getList()
# Aの各数字の（２進数における）各桁ごとに分解して排他的論理和を求める
# 例
# 3
# 1 2 3 →
# 1, 10, 11
# 2 ** 0の桁について(1 ^ 2) 1 ^ 0 = 1,(1 ^ 3) 1 ^ 1 = 0,(2 ^ 3) 0 ^ 1 = 1
# 2 ** 1の桁について 0(1の2 ** 1の桁は0) ^ 1 = 1, 0 ^ 1 = 1, 1 ^ 1 = 0
# 各桁について2 ** iの桁が1の数字の選び方 * 2 ** iの桁が0の数字の選び方 * 2 ** iを
# 足し合わせる
lista = [[0, 0] for i in range(61)]
# bitの各桁が１か０かをlistaに収納
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            lista[i][1] += 1
        else:
            lista[i][0] += 1
for i in A:
    splitbit(i)
ans = 0
for i in range(61):
    ans += ((lista[i][0] * lista[i][1]) * (2 ** i)) % mod
print(ans % mod)
