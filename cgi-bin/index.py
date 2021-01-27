from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# パ研合宿2020　第1日「SpeedRun」
# 同じgcdを持つ区間は結合しても同じまま

"""
K個に切り分ける
それぞれの部分の総和のgcdが大きいほどいい
最大公約数はいくつになるか
二分探索したいが dpもしたい

300C150とかは無理

K = 1から考える
答えはAの総和

A が最大300しかない
エッジを貼る
k回辺を移動して0 ~ Nにいけるか

調和級数
"""

N = getN()
A = [0] + getList()
su = sum(A)
for i in range(1, N + 1):
    A[i] += A[i - 1]

ans = [0] * (N + 1)
for i in range(su + 1, 0, -1):
    # これを通過すると必ず条件を満たす区間を作れる
    if su % i != 0:
        continue

    cnt = 0
    last = 0
    for j in range(1, N + 1):
        if (A[j] - A[last]) % i == 0:
            last = j
            cnt += 1

    # cnt以下の区間は結合することで簡単に作れる
    for a in range(cnt + 1):
        ans[a] = max(ans[a], i)

for a in ans[1:]:
    print(a)

# Chokudai SpeedRun 002 J - GCD β

"""
N <= 50000 これはなに？
NlogNまでならいける
最大公約数を最大にするには　同じ倍数でまとめればいい
ただしAiは大きい
どちらの数字を使うか
targetを選択するか
全部因数分解して候補を探る Aiがでかいので間に合わない
まずAi, Bi 10 ** 5個が候補としてある
1個下の奴とのgcdで結ぶ　エッジは高々20万本
AiスタートとBiスタートがある
残っているものとgcdする
Aiがでかいので...
A0, B0の約数しか候補にならない
"""

def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

N = getN()
A, B = [], []
for i in range(N):
    a, b = getNM()
    A.append(a)
    B.append(b)

ans = set()
opt_l = make_divisors(A[0]) + make_divisors(B[0])

for opt in opt_l:
    for i in range(N):
        if (A[i] % opt != 0) and (B[i] % opt != 0):
            break
    else:
        ans.add(opt)

ans = sorted(list(ans))
print(ans[-1])
