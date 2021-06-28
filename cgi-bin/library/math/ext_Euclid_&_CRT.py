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

# ABC186 E - Throne

T = getN()
for _ in range(T):
    N, S, K = getNM()
    # Nx + Ky = N - Sになるようなx, yを求める
    ans = form_ext(N, K, N - S)
    if ans[0] == 0:
        print(-1)
    else:
        print(ans[1][3] % abs(ans[1][2]))

# 中国剰余定理
# x = b1 (mod m1)
# x = b2 (mod m2)
# を両方満たす整数xが0 ~ m1 * m2内にただ一つ存在する
# そのようなxを求める
# 例 x = 0 (mod 2)
# 　 x = -1 (mod 11)
# の場合答えは10

# 計算量logN
def CRT(b1, m1, b2, m2):
    # 拡張ユークリッド
    def extGcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = extGcd(b % a, a)
        return g, x - (b // a) * y, y

    d, p, q = extGcd(m1, m2)
    if (b2 - b1) % d != 0:
        return 0, -1
    m = m1 * (m2 // d) # 最小公倍数
    tmp = (b2 - b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return r, m

# (1 + 2 +...+k) = aN
# k(k + 1) = 2aN　になる最小のkを求めたい
# N = 11なら22, 44, 66,...110 = 10 * (10 + 1) k = 10が答え

# kとk + 1は互いに素なので(同じ因数xを持つなら、間がxの倍数分空いてないといけないので)
# 2Nを素因数分解する時、各素因子はKとK+1に振り分けられる
# 2つに振り分けた結果AとBができる（AB = 2N) A,Bに足らない因子はaで調整できる
# これがそれぞれk, k + 1になればいい
# つまりk = A * (aの因子)、k + 1 = B * (aの因子)

# K = 0 (mod A), K = -1 (mod B)となる最小のkを求めればいい
# 2Nの約数について全探索

def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

# ACLC B - Sum is Multiple
# CRTする

n = getN()
div = make_divisors(2 * n)
res = float('inf')
for x in div:
    y = 2 * n // x
    k = CRT(0, x, -1, y)
    if k[0] != 0:
        res = min(res, k[0])
print(res)
