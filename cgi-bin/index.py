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

# O(n)までOK a, b, cどれかを固定（ループ）させる
N, K = getNM()
# Kで割ってi余る数リスト
lista = [0] * K
ans = 0
for i in range(1, N + 1):
    lista[i % K] += 1
# 例えばN = 5, K = 3のとき1と４、2と5は同じものとして扱う
for a in range(K):
    # a（あまりがaであるもののどれか）に対応するb, cは
    # b == k - a(mod K)
    b = (K - a) % K
    c = (K - a) % K
    if (b + c) % K == 0:
        ans += lista[a] * lista[b] * lista[c]
print(ans)

# O(1)でやる場合
# a + b and b + c and c + a (mod k) ⇄
# a == b == c (mod k)
# また a + b == 0 と上記 a == bより
# a + b == 0 (mod K) ⇄ a + a == (mod K)
# ⇄ 2a == 0 (mod K)

# Kが奇数のとき
# Kの約数に2がないのでaがKで割り切れる必要がある
# よってKが奇数のとき問題の条件を満たすのはx ** 3通りある

# Kが偶数の時
# aがKで割り切れる、またはあまりがK / 2である必要がある
