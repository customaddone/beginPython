from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(1000000)
INF = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# M-sol プロコン　E - Product of Arithmetic Progression

"""
1000003 随分小さい　1000003の項の倍数があったら答えは0
lognで答えましょう
積はいくつか nがでかいのでまとめてO(1)で計算できるやつがある

7の場所を選ぶ　そのほかについて掛けて足し合わせ　これをまとめて

全てのクエリがd = 1の場合
x * (x + 1) + ...(x + n - 1)を求める
x以前の部分で割る
(x + n - 1)! / (x - 1)!を求める　階乗とその逆元を前計算しておく
dが1でない時は
各項をdで割るとうまくできる あとでd^nで掛ける
x/d, x/d + 1,...x/d + (n - 1)

連続する整数の掛け算はproductを考える　うまくproductにできないか
"""

MOD = 10** 6 + 3
fact = [1]

for i in range(1, 2 * MOD + 10):
    fact.append(fact[-1] * i % MOD)

for _ in range(int(input())):
    x, d, n = map(int, input().split())

    if x == 0:
        print(0)
        continue

    if d == 0:
        print(pow(x, n, MOD))
        continue

    if n > MOD:
        print(0)
        continue

    # dの逆元で割る
    a = x * pow(d, MOD - 2, MOD) % MOD
    ans = pow(d, n, MOD) * fact[a + n - 1] * pow(fact[a - 1], MOD - 2, MOD) % MOD
    print(ans)
