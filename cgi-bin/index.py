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


n, m = map(int, input().split())
lista = []
for i in range(n):
    a = getList()
    lista.append(a)

res = 0
for i in range(m):
    for j in range(i + 1, m):
        # 集計
        tmp = 0
        # 入力されたものをループさせて、それぞれの場合の値を求める
        for k in range(n):
            tmp += max(lista[k][i], lista[k][j])
        res = max(res, tmp)
print(res)
