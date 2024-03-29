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
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

class Rational():
    def __init__(self, nume, deno):
        # 約分して格納
        self.n = self.reduction(nume, deno)

    # 約分 denoが0でもいける
    def reduction(self, nume, deno):
        g = math.gcd(nume, deno)
        if g == 0:
            g = 1
        if deno < 0:
            return (-(nume // g), -(deno // g))
        else:
            return (nume // g, deno // g)

    # たす
    def __add__(self, other):
        nume = self.n[0] * other.n[1] + self.n[1] * other.n[0]
        deno = self.n[1] * other.n[1]
        return Rational(nume, deno)

    # ひく
    def __sub__(self, other):
        nume = self.n[0] * other.n[1] - self.n[1] * other.n[0]
        deno = self.n[1] * other.n[1]
        return Rational(nume, deno)

    # かける
    def __mul__(self, other):
        return Rational(self.n[0] * other.n[0], self.n[1] * other.n[1])

    # わる 「/」の方
    def __truediv__(self, other):
        return Rational(self.n[0] * other.n[1], self.n[1] * other.n[0])

# a >= bかな？
def a_bigger(a, b):
    return a[0] * b[1] - a[1] * b[0] >= 0

# マージソート O(NlogN)だけど処理遅そう
def merge_sort(x):
    retary = []
    if len(x) <= 1:
        retary.extend(x)
    else:
        m = len(x) // 2
        # 逆にする
        first = merge_sort(x[:m])[::-1]
        second = merge_sort(x[m:])[::-1]
        while len(first) > 0 and len(second) > 0:
            # 小さい方を取り出してappendする
            if a_bigger(first[-1].n, second[-1].n):
                retary.append(second.pop())
            else:
                retary.append(first.pop())
        # 元に戻して繋げる
        retary.extend(first[::-1] if len(first) > 0 else second[::-1])

    return retary

# ABC115 C - Christmas Eve

N, K = getNM()
K -= 1
A = getArray(N)
A = [Rational(a, 1) for a in A]
A = merge_sort(A)

ans = inf
for i in range(N - K):
    ans = min(ans, A[i + K].n[0] - A[i].n[0])
print(ans)

# 個別ver
# 約分 denoが0でもいける
def reduction(nume, deno):
    g = math.gcd(nume, deno)
    if g == 0:
        g = 1
    if deno < 0:
        return (-(nume // g), -(deno // g))
    elif deno > 0:
        return (nume // g, deno // g)
    # n / 0 inf
    else:
        return (1, 0)

# たす
def add(self, other):
    nume = self[0] * other[1] + self[1] * other[0]
    deno = self[1] * other[1]
    if deno == 0:
        nume = 1
    return (nume, deno)

# ひく
def sub(self, other):
    nume = self[0] * other[1] - self[1] * other[0]
    deno = self[1] * other[1]
    if deno == 0:
        nume = 1
    return (nume, deno)

# かける
def mul(self, other):
    nume = self[0] * other[0]
    deno = self[1] * other[1]
    if deno == 0:
        nume = 1
    return (nume, deno)

# わる 「/」の方
def truediv(self, other):
    nume = self[0] * other[1]
    deno = self[1] * other[0]
    if deno == 0:
        nume = 1
    return (nume, deno)

# a >= bかな？
def a_bigger(a, b):
    return a[0] * b[1] - a[1] * b[0] >= 0

# 同じかな？
def equal(a, b):
    return a[0] * b[1] - a[1] * b[0] == 0

# 有理数ver
# 二つの点を通る直線の方程式を求める
# y = line[0]x + line[1]
# 傾きmaxならx = line[3]
def line(Ax, Ay, Bx, By):
    if Ay == By:
        return (0, 1), Ay, (None, 1)
    if Ax == Bx:
        return (1, 0), (0, 1), Ax
    a = truediv(sub(Ay, By), sub(Ax, Bx))
    b = sub(Ay, mul(a, Ax))
    # ちゃんと約分する
    return reduction(a[0], a[1]), reduction(b[0], b[1]), (None, 1)

# マージソート O(NlogN)だけど処理遅そう
def merge_sort(x):
    retary = []
    if len(x) <= 1:
        retary.extend(x)
    else:
        m = len(x) // 2
        # 逆にする
        first = merge_sort(x[:m])[::-1]
        second = merge_sort(x[m:])[::-1]
        while len(first) > 0 and len(second) > 0:
            # 小さい方を取り出してappendする
            if a_bigger(first[-1], second[-1]):
                retary.append(second.pop())
            else:
                retary.append(first.pop())
        # 元に戻して繋げる
        retary.extend(first[::-1] if len(first) > 0 else second[::-1])

    return retary

#### a >= bかな？　全順序ならマージソートできる ######
def a_bigger(a, b):
    return a >= b

# 同じかな？
def equal(a, b):
    return a[0] * b[1] - a[1] * b[0] == 0
###############################################

# マージソート + 転倒数
def merge_sort(x):
    retary = []
    res_rev = 0
    if len(x) <= 1:
        retary.extend(x)
    else:
        m = len(x) // 2
        # 逆にする
        f, s = merge_sort(x[:m]), merge_sort(x[m:])
        first, rev1 = f[0][::-1], f[1]
        second, rev2 = s[0][::-1], s[1]
        res_rev += (rev1 + rev2)
        while len(first) > 0 and len(second) > 0:
            # 小さい方を取り出してappendする
            if a_bigger(first[-1], second[-1]):
                retary.append(second.pop())
                res_rev += len(first)
            else:
                retary.append(first.pop())
        # 元に戻して繋げる
        retary.extend(first[::-1] if len(first) > 0 else second[::-1])

    return retary, res_rev
