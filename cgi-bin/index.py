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
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
inf = float('inf')
eps = 10 ** (-12)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
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
    return a.n[0] * b.n[1] - a.n[1] * b.n[0] >= 0

# 同じかな？
def equal(a, b):
    return a.n[0] * b.n[1] - a.n[1] * b.n[0] == 0
"""

# 約分 denoが0でもいける
def reduction(nume, deno):
    g = math.gcd(nume, deno)
    if g == 0:
        g = 1
    if deno < 0:
        return (-(nume // g), -(deno // g))
    else:
        return (nume // g, deno // g)

# たす
def add(self, other):
    nume = self[0] * other[1] + self[1] * other[0]
    deno = self[1] * other[1]
    return (nume, deno)

# ひく
def sub(self, other):
    nume = self[0] * other[1] - self[1] * other[0]
    deno = self[1] * other[1]
    return (nume, deno)

# かける
def mul(self, other):
    return (self[0] * other[0], self[1] * other[1])

# わる 「/」の方
def truediv(self, other):
    return (self[0] * other[1], self[1] * other[0])

# a >= bかな？
def a_bigger(a, b):
    return a[0] * b[1] - a[1] * b[0] >= 0

# 同じかな？
def equal(a, b):
    return a[0] * b[1] - a[1] * b[0] == 0

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

"""
Kが1なら無数に存在
(1, 0): inf
(0, 1): 0(零元)
(1, 1): 1(単位元)
"""

N, K = getNM()
P = []
for i in range(N):
    x, y = getNM()
    # 有理数体に
    P.append([(x, 1), (y, 1)])
s = set()
if K == 1:
    print('Infinity')
    exit()
for i in range(N):
    for j in range(i + 1, N):
        s.add(line(P[i][0], P[i][1], P[j][0], P[j][1]))

ans = 0
for a, b, ver in s:
    cnt = 0
    for x, y in P:
        # 垂直
        if a == (1, 0):
            cnt += (equal(x, ver))
        else:
            cnt += (equal(y, add(mul(a, x), b)))
    if cnt >= K:
        ans += 1
print(ans)
