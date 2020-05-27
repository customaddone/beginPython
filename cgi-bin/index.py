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

N, M = map(int, input().split())
lista = []
for i in range(M):
    k, *s, = map(int, input().split())
    lista.append(list(s))
P = list(map(int, input().split()))

sumans = 0

for bit in range(1 << N):
    # 各状態でフラグを立てる
    flag = True
    # 条件についてループ
    for i in range(M):
        sum = 0
        for j in lista[i]:
            if bit & (1 << (j - 1)):
                sum += 1
        if sum % 2 != P[i]:
            flag = False
            break
    # 判定
    if flag:
        sumans += 1
print(sumans)
