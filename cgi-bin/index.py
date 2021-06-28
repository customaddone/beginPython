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
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ユークリッド互除法
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

# 最小公倍数
def lcm(x, y):
    return x * (y // math.gcd(x, y))

"""
ユークリッド互除法の原理

非負整数a, bがある
b = qa + r(q, rは0以上の整数)

dをa % d == 0, r % d == 0となる自然数とする
すると(qa + r) % d == 0となり、b = qa + rなので、
bはdで割れて、aとrの公約数は全てbを割り切る（aとrの公約数は全てaとbの公約数に含まれる）

逆に、eをb % e == 0、a % e == 0となる自然数とすると
b - qa = rより上と同じように上とは逆のことを行える
bとaの公約数は全てrを割り切る（bとaの公約数は全てaとrの公約数に含まれる）

したがって、aとbの公約数全体 = aとrの公約数全体
"""

# 拡張ユークリッド
# ax + by = gとなる
# (g, x, y)を返す

# 一般式はa, bをgcd(a, b)で割った上で
# (x, y) = (-b * t + x, -a * t + y) tは任意の整数
# 111x + 30y = 12の場合
# extGcd(a, b)(g, x, yとする) = (3, 12, -44)で
# 111, 30をgで割った上で
# (x, y) = (-10t + 12, -37t - 44)
def extGcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = extGcd(b % a, a)
    return g, x - (b // a) * y, y

# ax + by = cとなる(x, y)の一般項を求めてくれる
def form_ext(a1, b1, c):
    def extGcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = extGcd(b % a, a)
        return g, x - (b // a) * y, y
    g, x, y = extGcd(a1, b1)
    # 解なし
    if c % g != 0:
        return 0, []

    x *= c // g
    y *= c // g
    a2 = a1 // g
    b2 = b1 // g

    return 1, [-b2, x, -a2, y]

"""
一次不定方程式ax + by = cの整数解を求める

一次不定方程式ax + by = cが整数解をもつ必要十分条件はcがgcd(a, b)で割り切れることである

d = gcd(a, b)とするとaもbもdで割り切れるため、ax + by(= c)もdで割り切れる
一次不定方程式ax + by = cが整数解をもつ（cが何らかの整数になる）なら
cがgcd(a, b)で割り切れる

111x + 30y = 12の(x, y)を求める
ユークリッドするとgcd(111, 30) = 3 ここからスタートしてユークリッドを遡る
3 = 21 - 2 * 9 # 21 % 9 = 3
  = 21 - 2 * (30 - 1 * 21) # 30 % 21
  = (-2) * 30 + 3 * 21...
すると、(x, y) = (3, -11)が111x + 30y = 3を満たす
これをそれぞれ4倍すればいい
一つ解を求めたら代入して = 0の形にする　一般項が求められる
"""

T = getN()
for _ in range(T):
    N, S, K = getNM()
    # Nx + Ky = N - Sになるようなx, yを求める
    ans = form_ext(N, K, N - S)
    if ans[0] == 0:
        print(-1)
    else:
        print(ans[1][3] % abs(ans[1][2]))
