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

N = getN()
A = [-1] + getList()
lista = [0 for i in range(N + 1)]

# 逆順に実施する
# 1からループ回さないと34行目でバグる
for i in range(1, N + 1)[::-1]:
    cnt = 0
    # 2 * i, 3 * i...について
    for j in range(2 * i, N + 1, i):
        cnt += lista[j]
    # もしcnt % 2とa[i]が合わなければb[i]にボールを置いて修正
    if cnt % 2 != A[i]:
        lista[i] = 1
ans = []
for i in range(N + 1):
    if lista[i] == 1:
        ans.append(str(i))
print(len(ans))
print(" ".join(ans))
